from setuptools import setup
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-ersatz-table-valued-functions",
    description="Enable a limited form of table-valued functions.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Colin Dellow",
    url="https://github.com/cldellow/datasette-ersatz-table-valued-functions",
    project_urls={
        "Issues": "https://github.com/cldellow/datasette-ersatz-table-valued-functions/issues",
        "CI": "https://github.com/cldellow/datasette-ersatz-table-valued-functions/actions",
        "Changelog": "https://github.com/cldellow/datasette-ersatz-table-valued-functions/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License"
    ],
    version=VERSION,
    packages=["datasette_ersatz_table_valued_functions"],
    entry_points={"datasette": ["ersatz_table_valued_functions = datasette_ersatz_table_valued_functions"]},
    install_requires=["datasette", "ersatz-table-valued-functions", "datasette-rewrite-sql"],
    extras_require={"test": ["pytest", "pytest-asyncio", "pytest-watch"]},
    python_requires=">=3.7",
)
