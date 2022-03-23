import unittest
from keycreationmachine import KeyCreationMachine

class TestKeyCreationMachine(unittest.TestCase):
    def setUp(self):
        self.KCM = KeyCreationMachine()

    def test_generate_random_bits_length_correct(self):
        random_bit_number = self.KCM.generate_random_bits(1024)
        l = len(bin(random_bit_number))-2

        self.assertEqual(0, 1024)
