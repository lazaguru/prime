import unittest
from Prime import *


class PrimeTest(unittest.TestCase):
	def setUp(self):
		self.prime = Prime()

	def test_number_less_than_zero_not_prime(self):
		self.assertFalse(self.prime.isPrime(-1))

	def test_1_is_not_prime(self):
		self.assertFalse(self.prime.isPrime(1))

	def test_2_is_prime(self):
		self.assertTrue(self.prime.isPrime(2))

	def test_4_is_not_prime(self):
		self.assertFalse(self.prime.isPrime(4))

	def test_5_is_prime(self):
		self.assertTrue(self.prime.isPrime(5))

	def test_massive_number_is_prime(self):
		self.assertTrue(self.prime.isPrime(1066340417491710595814572169))

	def test_massive_even_number_is_not_prime(self):
		self.assertFalse(self.prime.isPrime(1066340417491710595814572168))


if __name__ == '__main__':
    unittest.main()