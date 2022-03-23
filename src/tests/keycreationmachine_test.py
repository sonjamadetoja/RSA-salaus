import unittest
from keycreationmachine import KeyCreationMachine as KCM

class TestKeyCreationMachine(unittest.TestCase):
    def setUp(self):
        pass

    def test_generate_random_bits_length_correct(self):
        random_bit_number = KCM.generate_random_bits(1024)
        l = len(bin(random_bit_number))-2

        self.assertEqual(l, 1024)
