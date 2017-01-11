import unittest
from animals import *

class TestAnimals(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        print('Set up class')
        self.animal = Animal()
        self.dog = Dog("Spot")
        self.dog.set_legs(4)

    def test_AnimalHasName(self):
        self.animal.name = "Fred"
        self.assertIsNotNone(self.animal.name)

    def test_SpeciesIsCorrect(self):
        self.animal.set_species("Amur Leopard")
        self.assertEqual(self.animal.species, "Amur Leopard")

    def test_AnimalIsInstanceOfAnimal(self):
        self.assertIsInstance(self.animal, Animal)

    def test_DogIsInstanceOfDog(self):
        self.assertIsInstance(self.dog, Dog)

    def test_DogWalkSpeedIsCorrect(self):
        self.dog.walk()
        self.assertEqual(self.dog.speed, 0.8)

    def test_AnimalWalkSpeedIsCorrect(self):
        self.animal.set_legs(2)
        self.animal.walk()
        self.assertEqual(self.animal.speed, 0.2)

if __name__ == '__main__':
    unittest.main()
