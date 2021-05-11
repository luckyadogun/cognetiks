from typing import List

class DataAttributeError(Exception): pass

class NamesDB:
    def __init__(self, data: List) -> None:
        self.data = data
        self._check_data()

    def _check_data(self):
        if not isinstance(self.data, (list, tuple)):
            raise DataAttributeError("<data> argument must be a <<list>> or <<tuple>> type")

        if len(self.data) == 0:
            raise DataAttributeError("<data> argument must not be empty")