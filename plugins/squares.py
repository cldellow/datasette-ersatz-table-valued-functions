from datasette import hookimpl
from datasette_ersatz_table_valued_functions import create_table_function

def tbl_squares(n):
    return [(i, i*i) for i in range(n)]

@hookimpl
def startup():
    create_table_function('tbl_squares', 1, tbl_squares, ['root', 'square'])
