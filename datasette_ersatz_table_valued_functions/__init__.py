import json
from datasette import hookimpl
from datasette.database import Database
from ersatz_table_valued_functions import rewrite

all_functions = []
mappings = {}

def create_table_function(name, narg, func, column_names):
    mappings[name.upper()] = column_names
    all_functions.append((name, narg, func, column_names))

original_execute = Database.execute
async def patched_execute(
    self,
    sql,
    params=None,
    truncate=False,
    custom_time_limit=None,
    page_size=None,
    log_sql_errors=True,
):
    return await original_execute(
        self,
        rewrite(sql, mappings),
        params,
        truncate,
        custom_time_limit,
        page_size,
        log_sql_errors
    )

Database.execute = patched_execute

@hookimpl
def prepare_connection(conn, database):
    for name, narg, func, column_names in all_functions:
        def wrapper(*args, **kwds):
            return json.dumps(func(*args, **kwds))

        conn.create_function(name, narg, wrapper)
