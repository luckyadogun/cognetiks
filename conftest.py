import pytest

from src.section_one.names_db import NamesDB

@pytest.fixture
def names_list(scope="class", autouse=True):
    return ['Alice', 'Bob', 'Jeremy', 'Sam', 'Henry', 'Sarah', 'Ashley']