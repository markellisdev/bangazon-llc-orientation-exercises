import unittest
from superheroPart3 import *

class TestSuperman(unittest.TestCase):

	@classmethod
	def setUpClass(self):
		print('Set up class')
		self.superman = Superman()

	def test_SupermanMustBeBulletproof(self):
#		superman = Superman() Now unecessary after @classmethod setUpClass
		self.assertTrue(self.superman.is_bulletproof)

	def test_SupermanIsFlyingFast(self):
#		superman = Superman()
		self.assertEqual(self.superman.air_speed, 1000000)

	def test_SupermanIsSwimmingFast(self):
#		superman = Superman()
		self.assertEqual(self.superman.water_speed, 250)

	def test_SupermanIsASuperhero(self):
#superman = Superman() #first need to create instance of Superman
		self.assertIsInstance(self.superman, Superhero)

	def test_SupermanIsAFlyingSuperhero(self):
		self.assertIsInstance(self.superman, Flying)
#superman = Superman()
#first need to create instance of Superman


if __name__ == '__main__':
    unittest.main()
