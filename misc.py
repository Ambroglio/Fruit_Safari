import sys, inspect
import fruit_cells
import re

class Misc:
    def getFruits(self) -> list:
        fruits = []

        for name, obj in inspect.getmembers(sys.modules["fruit_cells"]):
            if inspect.isclass(obj):
                print(name)
                if re.match(r"^(?!Fruit).+Cell", name):
                    fruits += [obj()]

        print(fruits)

        return fruits