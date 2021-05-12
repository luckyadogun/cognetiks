import textwrap
from typing import List, Union


class DataAttributeError(Exception):
    pass


class NamesDB:
    def __init__(self, data: List) -> None:
        self.data = data
        self._check_data()

    def _check_data(self):
        if not isinstance(self.data, (list, tuple)):
            raise DataAttributeError(
                "<data> argument must be a <<list>> or <<tuple>> type"
            )

        if len(self.data) == 0:
            raise DataAttributeError(
                "<data> argument must not be empty"
            )

    def list_names(self):
        for name in self.data:
            print(
                textwrap.dedent(
                    """\f"Hello my name is {name}\n"""
                )
            )

    def list_names_at_pos(
        self, pos: List[Union[list, int]]
    ):
        """
        Polymorphic method: position can be an int or a list of ints
        """
        if not isinstance(pos, (list, int)):
            raise DataAttributeError(
                "<pos> argument must be a <<list>> or <<int>> type"
            )

        if isinstance(pos, list) and len(pos) == 0:
            raise DataAttributeError(
                "<data> argument must not be empty"
            )

        if isinstance(pos, list):
            for items in pos:
                if not isinstance(items, int):
                    raise DataAttributeError(
                        "list <data> argument must a list of integers"
                    )
                return [
                    self.data[index - 1] for index in pos
                ]

        return [self.data[pos - 1]]

    def reverse_list_names(self):
        return list(reversed(self.data))
