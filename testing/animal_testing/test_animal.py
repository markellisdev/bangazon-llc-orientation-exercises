import unittest
from animals import *

class TestAnimals(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        self.animal = Animal()
        self.dog = Dog("Spot")

    def test_AnimalHasName(self):
        self.animal.name = "Fred"
        self.assertIsNotNone(self.animal.name)

    def test_SpeciesIsCorrect(self):
        self.animal.set_species("Amur Leopard")
        self.assertEqual(self.animal.species, "Amur Leopard")

if __name__ == '__main__':
    unittest.main()
