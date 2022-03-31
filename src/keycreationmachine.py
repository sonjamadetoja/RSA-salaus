import random
ticket = random.SystemRandom()
# from math import sqrt

class KeyCreationMachine:
    """Tämä luokka sisältää funktiot, joita tarvitaan salausavainparin luomiseen.
    """
    def __init__(self):
        """Tämä on luokan konstruktori.
        """

    def generate_random_bits(self, length):
        """Tämä funktio luo halutun pituisen satunnaisluvun.

        Args:
            length (int): Haluttu bittien määrä.

        Returns:
            int: satunnaisluku
        """
        return ticket.randrange(2**(length-1)+1, 2**length-1)

    def check_if_prime(self, candidate, number_of_rounds):
        """Tämä funktio tarkistaa, onko annettu luku alkuluku.
        Testattava muuttuja on nimeltään candidate,
        ja se voidaan kirjoittaa muodossa 2**r·d + 1.
        Koska testi on probabilistinen, tehdää useita testikierroksia,
        ja sitä varten annetaan testikierrosten määrä.

        Args:
            candidate (int): Testattava luku.
            number_of_rounds (int): Testikierrosten määrä

        Returns:
            boolean: True tai False sen mukaan onko testattava luku alkuluku vai ei.
        """
        if candidate <= 3:
            return True
        if candidate % 2 == 0:
            return False
        d_even_number = candidate - 1
        r_twos_power = 0
        while d_even_number % 2 == 0:
            d_even_number >>= 1
            r_twos_power += 1
        d_even_number = int(d_even_number)
        for _ in range(number_of_rounds):
            random_integer_a = ticket.randrange(2, candidate-2)
            if not self.one_test(candidate, random_integer_a, d_even_number, r_twos_power):
                return False
        return True

    def one_test(self, candidate, random_integer_a, d_even_number, r_twos_power):
        """Tämä funktio tekee yhden probabilistisen Miller-Rabin-testin,
        joka testaa onko annettu luku alkuluku. Testattava luku voidaan
        kirjoittaa muodossa 2**r·d + 1.

        Args:
            candidate (int): testattava luku
            random_integer_a (int): satunnaisluku
            d_twos_multiplier (int): ylläolevan kaavan d
            r_twos_power (int): ylläolevan kaavan r

        Returns:
            boolean: True tai False
        """
        witness = pow(random_integer_a, d_even_number, candidate)
        if witness in (1, candidate-1):
            return True
        for _ in range(r_twos_power-1):
            witness = pow(witness, 2, candidate)
            if witness == (candidate-1):
                return True
        return False

    def generate_prime(self, length, number_of_rounds):
        """Tämä funktio luo alkuluvun.

        Args:
            length (int): alkuluvun haluttu pituus
            number_of_rounds (int): testauskierrosten määrä alkuluvuksi testaamista varten

        Returns:
            int: alkuluku
        """
        while True:
            candidate = self.generate_random_bits(length)
            result = self.check_if_prime(candidate, number_of_rounds)
            if result is True:
                return candidate

    # def generate_key(self):
    #     rand_bits = self.generate_random_bits(1024)
    #     result = self.miller_rabin_test(rand_bits, 100)
    #     ...jotain...
    #     return jotain
