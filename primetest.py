import unittest
from primenumbergen import is_prime

class PrimesTest(unittest.TestCase):
	def setUp(self):
        self.prime = is_Prime()
    """Tests for `primenumgen.py`."""
    def test_is_four_non_prime(self):
    """Is four correctly determined not to be prime?"""
        self.assertFalse(is_prime(4), msg='Four is not prime!')
    def test_is_zero_not_prime(self):
    """Is zero correctly determined not to be prime?"""
        self.assertFalse(is_prime(0))
    def test_input_zero(self):
        self.assertRaises(Exception):
            get_primes(0)

    def test_input_one(self):
        self.assertRaises(Exception):
            get_primes(1)

    def test_list_is_not_greater_than_n(self):
        list_returned = get_primes(100)
        self.assertTrue(len(list_returned) < 100)
    def test_number_less_than_zero_not_prime(self):
        self.assertFalse(self.prime.isPrime(-1)) 
    def test_1_is_not_prime(self):
        self.assertFalse(self.prime.isPrime(1))
    def test_5_is_prime(self):
        self.assertTrue(self.prime.isPrime(5)) 
    def test_massive_number_is_prime(self):
        self.assertTrue(self.prime.isPrime(1066340417491710595814572169))

    def test_massive_even_number_is_not_prime(self):
        self.assertFalse(self.prime.isPrime(1066340417491710595814572168))


if __name__ == '__main__':
    unittest.main()              