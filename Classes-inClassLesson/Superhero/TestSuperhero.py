import unittest
from superhero import *

class TestSuperhero(unittest.TestCase):

    def test_SuperheroMustHaveNameProperty(self):

        random_superhero = Superhero("Will Smith") #first need to create instance of Superhero
        self.assertEqual(random_superhero.name, "Will Smith")

    def test_SuperheroAddPowerMustIncludePower(self):

        random_superhero = Superhero("Clark")
        random_superhero.add_power("Invisibility")
        self.assertIn("Invisibility", random_superhero.powers)

if __name__ == '__main__':
    unittest.main()
