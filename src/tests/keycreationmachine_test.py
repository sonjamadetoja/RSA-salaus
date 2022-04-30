import unittest
from keycreationmachine import KeyCreationMachine
from keypair import KeyPair

class TestKeyCreationMachine(unittest.TestCase):
    def setUp(self):
        self.KCM = KeyCreationMachine()

    def test_generate_random_bits_length_correct(self):
        random_bit_number = self.KCM.generate_random_bits(1024)
        l = len(bin(random_bit_number))-2

        self.assertEqual(l, 1024)

    def test_check_if_prime_true(self):
        result = self.KCM.check_if_prime(11, 40)
        self.assertEqual(result, True)
        result = self.KCM.check_if_prime(541, 40)
        self.assertEqual(result, True)
        result = self.KCM.check_if_prime(427993, 40)
        self.assertEqual(result, True)
        result = self.KCM.check_if_prime(1034233, 40)
        self.assertEqual(result, True)
        result = self.KCM.check_if_prime(19134702400093278081449423917, 40)
        self.assertEqual(result, True)
        result = self.KCM.check_if_prime(11111111111111111111111, 40)
        self.assertEqual(result, True)
        result = self.KCM.check_if_prime(56713727820156410577229101238628035243, 40)
        self.assertEqual(result, True)
        result = self.KCM.check_if_prime(179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137859, 40)
        self.assertEqual(result, True)
        result = self.KCM.check_if_prime(203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790123203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790837, 40)
        self.assertEqual(result, True)
        result = self.KCM.check_if_prime(203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790123, 40)
        self.assertEqual(result, True)

    def test_check_if_prime_false(self):
        result = self.KCM.check_if_prime(1, 1)
        self.assertEqual(result, False)
        result = self.KCM.check_if_prime(333, 40)
        self.assertEqual(result, False)
        result = self.KCM.check_if_prime(990640698243, 40)
        self.assertEqual(result, False)
        result = self.KCM.check_if_prime(203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790121, 40)
        self.assertEqual(result, False)
        result = self.KCM.check_if_prime(203956878356401977405765866929034577280193993314348263094772646453283062722701277632936616063144088173312372882677123879538709400158306567338328279154499698366071906766440037074217117805690872792848149112022286332144876183376326512083574821647933992961249917319836219304274280243803104015000563790125, 40)
        self.assertEqual(result, False)
        result = self.KCM.check_if_prime(179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224137859179769313486231590772930519078902473361797697894230657273430081157732675805500963132708477322407536021120113879871393357658789768814416622492847430639474124377767893424865485276302219601246094119453082952085005768838150682342462881473913110540827237163350510684586298239947245938479716304835356329624224138295, 40)
        self.assertEqual(result, False)

    def test_check_if_prime_very_small(self):
        result = self.KCM.check_if_prime(2, 1)
        self.assertEqual(result, True)
        result = self.KCM.check_if_prime(3, 1)
        self.assertEqual(result, True)

    def test_check_if_prime_divisible_by_two(self):
        result = self.KCM.check_if_prime(4, 1)
        self.assertEqual(result, False)
        result = self.KCM.check_if_prime(102, 1)
        self.assertEqual(result, False)
        result = self.KCM.check_if_prime(45000, 1)
        self.assertEqual(result, False)
        result = self.KCM.check_if_prime(490832, 1)
        self.assertEqual(result, False)
        result = self.KCM.check_if_prime(8432917483274932, 1)
        self.assertEqual(result, False)

    def test_generate_prime(self):
        prime = self.KCM.generate_prime(1024)
        length_of_p = len(bin(prime))-2

        self.assertEqual(type(prime), int)
        self.assertEqual(length_of_p, 1024)

    def test_generate_key_parts(self):
        int_n, int_e, int_d = self.KCM.generate_key_parts()
        modulo_value = 1**int((int_e*int_d)%int_n)

        self.assertEqual(int_e, 65537)
        self.assertEqual(modulo_value, 1)

    def test_generate_key_pair(self):
        test_key_pair = self.KCM.generate_key_pair()
        int_n, int_e, int_d = test_key_pair.get_all_parts()
        modulo_value = 1**int((int_e*int_d)%int_n)
        test_type = type(test_key_pair)
        desired_type = type(KeyPair(0,0,0))

        self.assertEqual(int_e, 65537)
        self.assertEqual(modulo_value, 1)
        self.assertEqual(test_type, desired_type)

    def test_sieve_of_eratosthenes(self):
        result = self.KCM.sieve_of_eratosthenes(50)

        self.assertEqual(result, [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47])
