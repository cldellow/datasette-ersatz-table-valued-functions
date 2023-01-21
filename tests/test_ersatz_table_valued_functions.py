from datasette.app import Datasette
from datasette_ersatz_table_valued_functions import create_table_function
import pytest

def tbl_squares(n):
    return [(i, i*i) for i in range(n)]

@pytest.mark.asyncio
async def test_plugin_is_installed():
    create_table_function('tbl_squares', 1, tbl_squares, ['root', 'square'])
    datasette = Datasette(memory=True)
    response = await datasette.client.get("/-/plugins.json")
    assert response.status_code == 200
    installed_plugins = {p["name"] for p in response.json()}
    assert "datasette-ersatz-table-valued-functions" in installed_plugins

    db = datasette.databases['_internal']
    results = await db.execute('SELECT * FROM tbl_squares(10) WHERE square % 2 = 0')
    results = [tuple(row) for row in results]
    assert results == [(0, 0), (2, 4), (4, 16), (6, 36), (8, 64)]
