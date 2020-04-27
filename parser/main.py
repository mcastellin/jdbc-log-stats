import click
import json
from terminaltables import AsciiTable

values = {}


def strms2time(time_str):
    return int(time_str[:-2].strip())


def load_stats(line):
    if "|statement|" not in line:
        # Return immediately if this is not a statement line
        return

    global values
    data = line.split("|")
    query = data[5]
    time_ms = data[3]

    if not query in values:
        values[query] = {
            "query": query,
            "avg_ms": 0,
            "tot_ms": 0,
            "sigma_ms": 0,
            "count": 0,
        }

    val = values[query]
    ms = strms2time(time_ms)
    val["tot_ms"] = val["tot_ms"] + ms
    val["count"] = val["count"] + 1
    val["avg_ms"] = val["tot_ms"] / val["count"]


def dict2arr(entry):
    return [entry["query"][:140], entry["count"], entry["tot_ms"], entry["avg_ms"]]


def resentry2json(entry):
    return {
        "query": entry[0],
        "count": entry[1],
        "total_ms": entry[2],
        "avg_ms": entry[3],
    }


def print_ttable(data):
    table = AsciiTable([["Query", "Count", "Total ms", "Avg ms"]] + data)
    print(table.table)


def print_json(data):
    json_output = {"results": list(map(resentry2json, data))}
    print(json.dumps(json_output, indent=4))


output_options = {"ttable": print_ttable, "json": print_json}


def sortstat(sortkey, rows, outtype):
    val_list = list(values.values())

    table_data = sorted(val_list, key=lambda d: d[sortkey], reverse=True)
    outdata = list(map(dict2arr, table_data[:rows]))

    if outtype in output_options:
        output_options[outtype](outdata)
    else:
        print("Invalid output option specified")


@click.command()
@click.option("--file", help="The JDBC file path")
@click.option("--sort", default="avg_ms", help="The sort key")
@click.option("--rows", default=20, help="The number of rows to return")
@click.option("--output", default="ttable", help="The type of ouput: [ttable|json]")
def parseme(file, sort, rows, output):
    fd = open(file)
    for line in fd:
        load_stats(line)
    fd.close()

    sortstat(sort, rows, output)


if __name__ == "__main__":
    parseme()
