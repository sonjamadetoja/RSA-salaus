import random
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
        return random.randrange(2**(length-1)+1, 2**length-1)

    def check_if_prime(self, candidate, number_of_rounds):
        """Tämä funktio tarkistaa, onko annettu luku alkuluku.
        Testattava muuttuja on nimeltään candidate,
        ja se voidaan kirjoittaa muodossa 2**r·d + 1.

        Args:
            candidate (int): Tarkistettava luku.
            number_of_rounds (int): Testikierrosten määrä

        Returns:
            boolean: True tai False sen mukaan onko testattava luku alkuluku vai ei.
        """
        if candidate in (2,3):
            return True
        if candidate % 2 == 0:
            return False
        even_number = candidate - 1
        d_twos_multiplier = even_number / 2
        r_twos_power = 1
        while d_twos_multiplier % 2 == 0:
            d_twos_multiplier = d_twos_multiplier / 2
            r_twos_power += 1
        for i in range(number_of_rounds):
            i += 1
            random_integer_a = random.randint(2, candidate-2)
            x = random_integer_a % candidate
            if d_twos_multiplier % 2 == 1:
                x = x % candidate
            else:
                d_twos_multiplier = d_twos_multiplier/2
                x = (x*x)%candidate
            if x in (1, candidate-1):
                return True
            for j in range(r_twos_power-1):
                x = x**2 % candidate
                j += 1
                if x == (candidate-1):
                    return True
            return False
        return True
        # square_root_of_candidate = round(sqrt(candidate))
        # x:n nimi pitää muuttaa kuvaavammaksi

    def generate_prime(self, length, number_of_rounds):
        """Tämä funktio luo alkuluvun.

        Args:
            length (int): alkuluvun haluttu pituus
            number_of_rounds (int): testauskierrosten määrä alkuluvuksi testaamista varten

        Returns:
            _type_: alkuluku
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
