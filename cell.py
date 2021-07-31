import re


class Cell:
    def __init__(self):
        pass

    def __eq__(self, o: object) -> bool:
        return type(self) == type(o)

    def __str__(self) -> str:
        return re.split(r"Cell", self.__class__.__name__)[0].upper()

    def __hash__(self) -> int:
        return hash(str(self))