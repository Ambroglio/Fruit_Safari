from fruit_cells import AppleCell, BananaCell, BlackberryCell, GrapesCell, PeachCell, StrawberryCell
from settings import Settings
import unittest
import misc 

FRUITS = [AppleCell(), BananaCell(), BlackberryCell(), GrapesCell(), PeachCell(), StrawberryCell()]
FRUIT_WEIGHTS = [1, 1, 1, 1, 1, 1]

class FruitCellTest(unittest.TestCase):
    # careful; functions must start with TEST
    def testFruitNames(self):
        miscHandler = misc.Misc()
        fruits = miscHandler.getFruits()
        self.assertListEqual(fruits, FRUITS)

class SettingTest(unittest.TestCase):
    def testSettings(self):
        settings = Settings()
        self.assertEqual(settings.settings()["weight"], FRUIT_WEIGHTS)
        self.assertEqual(settings.settings()["cells"], FRUITS)

class NameTest(unittest.TestCase):
    def testName(self):
        a = AppleCell()
        self.assertEqual(str(a), "APPLE")

if __name__ == "__main__":
    unittest.main()