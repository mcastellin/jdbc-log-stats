# JDBC Logs Statistics from CLI
A python script that prints statistics for a given JDBC log file

## Prerequisites

- Python3
- Make

# Installation

Checkout this project on your MacOs or Linux envionrment and run the following:
```
cd jdbc-log-stats/
make all
```

# Printing JDBC Log Statistics

Locate your `jdbc.log` file and pass it as an argument to `bin/jdbcstats`, like so:
```
$ bin/jdbcstats --file /user/my/jdbc.log
```

## Additional options

For additional output options consult the command help
```
$ ./bin/jdbcstats --help
```
