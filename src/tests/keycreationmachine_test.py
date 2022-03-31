import unittest
from keycreationmachine import KeyCreationMachine

class TestKeyCreationMachine(unittest.TestCase):
    def setUp(self):
        self.KCM = KeyCreationMachine()

    def test_generate_random_bits_length_correct(self):
        random_bit_number = self.KCM.generate_random_bits(1024)
        l = len(bin(random_bit_number))-2

        self.assertEqual(l, 1024)

    def test_check_if_prime_true(self):
        result = self.KCM.check_if_prime(203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790123, 40)

        self.assertEqual(result, True)

    def test_check_if_prime_false(self):
        result = self.KCM.check_if_prime(203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790121, 40)

        self.assertEqual(result, False)

    def test_check_if_prime_less_than_three(self):
        result = self.KCM.check_if_prime(1, 1)

        self.assertEqual(result, True)

    def test_check_if_prime_divisible_by_two(self):
        result = self.KCM.check_if_prime(4, 1)

        self.assertEqual(result, False)

    def test_generate_prime(self):
        prime = self.KCM.generate_prime(1024)
        length_of_p = len(bin(prime))-2

        self.assertEqual(type(prime), int)
        self.assertEqual(length_of_p, 1024)
