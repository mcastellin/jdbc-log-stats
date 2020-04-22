import click
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


def sortstat(sortkey, rows=20):
    val_list = list(values.values())

    table_data = sorted(val_list, key=lambda d: d[sortkey], reverse=True)
    output = list(map(dict2arr, table_data[:rows]))
    table = AsciiTable([["Query", "Count", "Total ms", "Avg ms"]] + output)
    print(table.table)


@click.command()
@click.option("--file", help="The JDBC file path")
@click.option("--sort", default="avg_ms", help="The sort key")
@click.option("--rows", default=20, help="The number of rows to return")
def parseme(file, sort, rows):
    print(file)
    fd = open(file)
    for line in fd:
        load_stats(line)
    fd.close()

    sortstat(sort, rows)


if __name__ == "__main__":
    parseme()
