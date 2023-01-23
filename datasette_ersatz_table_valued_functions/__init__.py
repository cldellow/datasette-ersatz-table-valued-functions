import json
from datasette import hookimpl
from datasette.database import Database
from ersatz_table_valued_functions import rewrite

all_functions = []
mappings = {}

def create_table_function(name, narg, func, column_names):
    mappings[name.upper()] = column_names
    all_functions.append((name, narg, func, column_names))

@hookimpl
def rewrite_sql(fn, sql):
    if fn == 'execute':
        return rewrite(sql, mappings)

    # TOOD: also support execute_write* -- that requires changes in
    # ersatz_table_valued_functions to support multi-statement SQL strings.
    return sql

@hookimpl
def prepare_connection(conn, database):
    for name, narg, func, column_names in all_functions:
        def wrapper(*args, **kwds):
            return json.dumps(func(*args, **kwds))

        conn.create_function(name, narg, wrapper)
