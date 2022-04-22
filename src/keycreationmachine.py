import random
import math
from keypair import KeyPair
ticket = random.SystemRandom()



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
        Koska testi on probabilistinen, tehdään useita testikierroksia,
        ja sitä varten annetaan testikierrosten määrä.

        Args:
            candidate (int): Testattava luku.
            number_of_rounds (int): Testikierrosten määrä

        Returns:
            boolean: True tai False sen mukaan onko testattava luku alkuluku vai ei.
        """
        first_primes = self.sieve_of_eratosthenes(5000)
        if candidate in first_primes:
            return True
        if candidate == 1 or candidate % 2 == 0:
            return False
        d_even_number = candidate - 1
        r_twos_power = 0
        while d_even_number % 2 == 0:
            d_even_number >>= 1
            r_twos_power += 1
        d_twos_multiplier = int(d_even_number)
        for _ in range(number_of_rounds):
            random_integer_a = ticket.randrange(2, candidate-2)
            if not self.one_test(candidate, random_integer_a, d_twos_multiplier, r_twos_power):
                return False
        return True

    def sieve_of_eratosthenes(self, number):
        """Tämä funktio toteuttaa Eratostheneen seulan, joka antaa kaikki alkuluvut, jotka ovat pienempiä,
        kuin sille argumentiksi annettu luku (tässä number).

        Args:
            number (int): numero, jota pienemmät alkuluvut etsitään

        Returns:
            list: lista alkuluvuista
        """
        numbers = [True for i in range(2, number+2)]
        square_root = round(math.sqrt(number))+1
        for i in range(2, square_root):
            if numbers[i] is True:
                for j in range(pow(i,2), number, i):
                    numbers[j] = False
        primes = []
        for i in range(2, len(numbers)):
            if numbers[i] is True:
                primes.append(i)
        return primes

    def one_test(self, candidate, random_integer_a, d_twos_multiplier, r_twos_power):
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
        witness = pow(random_integer_a, d_twos_multiplier, candidate)
        if witness in (1, candidate-1):
            return True
        for _ in range(r_twos_power-1):
            witness = pow(witness, 2, candidate)
            if witness == (candidate-1):
                return True
        return False

    def generate_prime(self, length, number_of_rounds=40):
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

    def generate_two_different_primes(self):
        """Tämä funktio luo kaksi erilaista
        alkulukua kutsumalla alkuluvun luovaa
        funktiota kahdesti.

        Returns:
            tuple: monikko, joka sisältää kaksi erilaista alkulukua
        """
        while True:
            prime_p = self.generate_prime(1030)
            prime_q = self.generate_prime(1024)
            if prime_p != prime_q:
                return prime_p, prime_q

    def generate_key_parts(self):
        """Tämä funktio luo salausavainparin osat n, e ja d niin,
        että julkisen avaimen muodostavat n ja e, ja salaisen avaimen
        muodostavat n ja d.

        Returns:
            tuple: monikko, jonka ensimmäinen alkio on n, toinen e ja kolmas d
        """
        primes = self.generate_two_different_primes()
        prime_p = primes[0]
        prime_q = primes[1]
        int_n = prime_p*prime_q
        delta_p = prime_p-1
        delta_q = prime_q-1
        delta_n = self.calculate_lcm(delta_p, delta_q)
        int_e = 65537
        int_d = self.calculate_gcd_ext(int_e, delta_n)[1]
        return int_n, int_e, int_d

    def generate_key_pair(self):
        """Tämä funktio muodostaa avainparin luokan KeyPair
        avulla. Sen attribuutteja ovat modulus, julkisen avaimen
        eksponentti ja salaisen avaimen eksponentti.

        Returns:
            KeyPair: avainpari luokan KeyPair oliona
        """
        int_n, int_e, int_d = self.generate_key_parts()
        key_pair = KeyPair(int_n, int_e, int_d)
        return key_pair

    def calculate_gcd_ext(self, int_a, int_b):
        """Tämä funktio laskee kahden luvun /a ja b) suurimman yhteisen tekijän (syt eli gcd),
        sekä x:n ja y:n perustuen kaavaan ax + by = syt(a,b).
        Funktio perustuu laajennettuun Eukleideen algoritmiin.

        Args:
            int_a (int): luku
            int_b (int): luku

        Returns:
            tuple: monikko, jonka ensimmäinen alkio on syt, toinen x ja kolmas y
        """
        if int_a == 0:
            return int_b, 0, 1
        gcd, x_1, y_1 = self.calculate_gcd_ext(int_b%int_a, int_a)
        int_x = y_1 - (int_b//int_a)*x_1
        int_y = x_1
        return gcd, int_x, int_y

    def calculate_lcm(self, int_a, int_b):
        """Tämä funktio laskee kahden luvun pienimmän yhteisen jaettavan
        käyttäen hyväksi suurinta yhteistä jakajaa.

        Args:
            int_a (int): luku
            int_b (int): luku

        Returns:
            int: luku, joka on pienin yhteinen jaettava
        """
        gcd = self.calculate_gcd_ext(int_a, int_b)[0]
        return abs(int_a*int_b)//gcd
