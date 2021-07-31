from misc import Misc
from fruit_cells import *

class Settings:
    def __init__(self):
        miscHandler = Misc()
        
        self.__fruits = miscHandler.getFruits()
        self.__weight = []
        self.__minimumWidth = 2

        for i in range(0, len(self.__fruits)):
            self.__weight += [1]

    def settings(self) -> list:
        return {
            "cells": self.__fruits,
            "weight": self.__weight,
            "minimum_width": self.__minimumWidth
        }

    def changeMinimumWidth(self, minimumWidth):
        self.__minimumWidth = minimumWidth

    def changeWeight(self, newWeight, weightIndex):
        self.__weight[weightIndex] = newWeight