# datasette-ersatz-table-valued-functions

[![PyPI](https://img.shields.io/pypi/v/datasette-ersatz-table-valued-functions.svg)](https://pypi.org/project/datasette-ersatz-table-valued-functions/)
[![Changelog](https://img.shields.io/github/v/release/cldellow/datasette-ersatz-table-valued-functions?include_prereleases&label=changelog)](https://github.com/cldellow/datasette-ersatz-table-valued-functions/releases)
[![Tests](https://github.com/cldellow/datasette-ersatz-table-valued-functions/workflows/Test/badge.svg)](https://github.com/cldellow/datasette-ersatz-table-valued-functions/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/cldellow/datasette-ersatz-table-valued-functions/blob/main/LICENSE)

Enable a limited form of table-valued functions.

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-ersatz-table-valued-functions

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-ersatz-table-valued-functions
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
