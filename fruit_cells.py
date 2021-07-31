from cell import Cell

class FruitCell(Cell):
    """
    Fruit Cell is the core cell of the game !
    """
    def color(self) -> str:
        pass

class BananaCell(FruitCell):
    """
    Banana cell
    """
    def color(self) -> str:
        # yellow
        return "#ebec13"

class StrawberryCell(FruitCell):
    """
    Strawberry cell
    """
    def color(self) -> str:
        # red
        return "#e41e1b"

class PeachCell(FruitCell):
    """
    Peach cell
    """
    def color(self) -> str:
        # orange
        return "#e2891d"

class AppleCell(FruitCell):
    """
    Apple cell
    """
    def color(self) -> str:
        # green
        return "#6dd42b"

class BlackberryCell(FruitCell):
    """
    Blackberry cell
    """
    def color(self) -> str:
        # blue
        return "#1a67e5"

class GrapesCell(FruitCell):
    """
    Grapes cell
    """
    def color(self) -> str:
        # purple
        return "#c21ae5"