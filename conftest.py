import textwrap

import pytest

from src.section_one.names_db import NamesDB


@pytest.fixture
def names_list(scope="class", autouse=True):
    return [
        "Alice",
        "Bob",
        "Jeremy",
        "Sam",
        "Henry",
        "Sarah",
        "Ashley",
    ]


@pytest.fixture
def names_printed_dummy(names_list, auto_use=True):
    for name in names_list:
        print(
            textwrap.dedent(
                """\f"Hello my name is {name}\n"""
            )
        )


@pytest.fixture
def names_db_obj(names_list, auto_use=True):
    return NamesDB(data=names_list)
