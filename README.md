# datasette-ersatz-table-valued-functions

[![PyPI](https://img.shields.io/pypi/v/datasette-ersatz-table-valued-functions.svg)](https://pypi.org/project/datasette-ersatz-table-valued-functions/)
[![Changelog](https://img.shields.io/github/v/release/cldellow/datasette-ersatz-table-valued-functions?include_prereleases&label=changelog)](https://github.com/cldellow/datasette-ersatz-table-valued-functions/releases)
[![Tests](https://github.com/cldellow/datasette-ersatz-table-valued-functions/workflows/Test/badge.svg)](https://github.com/cldellow/datasette-ersatz-table-valued-functions/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/cldellow/datasette-ersatz-table-valued-functions/blob/main/LICENSE)

**ersatz** *(adj.)*: made or used as a substitute, typically an inferior one, for something else.

Enable a limited form of table-valued functions.

See also [ersatz-table-valued-functions](https://github.com/cldellow/ersatz-table-valued-functions/).

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-ersatz-table-valued-functions

## Usage

Write a plugin that registers a table-valued function in the `startup` hook:

```python
from datasette import hookimpl
from datasette_ersatz_table_valued_functions import create_table_function

def tbl_squares(n):
    return [(i, i*i) for i in range(n)]

@hookimpl
def startup():
    create_table_function('tbl_squares', 1, tbl_squares, ['root', 'square'])
```

You can then query this in Datasette:

```sql
SELECT root FROM tbl_squares(10) WHERE square % 2 = 0 AND square < 50
```

will emit 0, 2, 4, 6.

The parameters to the function can come from a subselect, which could target
any table and be arbitrarily complex:

```sql
SELECT root FROM tbl_squares((SELECT 10))
```

You can do whatever with the output of this function -- join it, aggregate it, etc.

What you can't do is use a join as the source of _input_ to the function:

```sql
WITH xs AS (SELECT 10 AS x) SELECT root FROM tbl_squares(x), xs
```

Queries that aren't supported are passed as-is to SQLite, which will itself
then reject them since no such table function is registered.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-ersatz-table-valued-functions
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
