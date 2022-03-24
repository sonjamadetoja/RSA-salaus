import random

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

    def miller_rabin_test(self, candidate, number_of_rounds):
        """Tämä funktio tarkistaa, onko annettu luku alkuluku.

        Args:
            candidate (int): Tarkistettava luku.
            number_of_rounds (int): Testikierrosten määrä
        """

    # def generate_key(self):
    #     rand_bits = self.generate_random_bits(1024)
    #     result = self.miller_rabin_test(randbits, 100)
    #     ...jotain...
    #     return jotain
