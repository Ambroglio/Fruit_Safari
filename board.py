from hashlib import new
from typing import Set
from settings import Settings
from cell import *
from fruit_cells import *
import random

class Board:
    def __init__(self, height: int, width: int, settings = Settings()):
        self.__height = height
        self.__width = width
        self.__board = []
        self.__settings = settings
        self.createBoard()

    def createBoard(self):
        print("CREATING")

        settings = self.__settings.settings()

        for i in range(0, self.__height):
            self.__board += [[None] * self.__width]

        print(self.__board)

        for i in range(0, self.__height):
            for j in range(0, self.__width):
                canBeSet = False
                newCell = None
                while not canBeSet:
                    newCell = self.pickCell()
                    self.__board[i][j] = newCell
                    line = []
                    for jBefore in range(j - settings["minimum_width"] + 1, j + 1):
                        if jBefore >= 0:
                            line += [self.__board[i][jBefore]]
                    column = []
                    for iBefore in range(i - settings["minimum_width"] + 1, i + 1):
                        if iBefore >= 0:
                            column += [self.__board[iBefore][j]]
                    print(i, j)
                    print(line)
                    print(column)
                    canBeSet = (len(line) < settings["minimum_width"] or len(set(line)) != 1) and (len(column) < settings["minimum_width"] or len(set(column)) != 1)
                    print(canBeSet)

        print(self.__board)

    def pickCell(self):
        settings = self.__settings.settings()
        return random.choices(settings["cells"], weights = settings["weight"])[0]

    def __str__(self) -> str:
        board = ""

        for line in self.__board:
            board += "|---|" * len(line) + "\n"
            for cell in line:
                print(cell)
                board += "|" + str(cell)[:3] + "|"
            board += "\n"

        board += "|---|" * len(self.__board[0])

        return board

    def setSettings(self, settings: Settings):
        self.__settings = settings

    def height(self):
        return self.__height

    def width(self):
        return self.__width

    def board(self):
        return self.__board

    def settings(self):
        return self.__settings