import random

class KeyCreationMachine:
    def __init__(self):
        pass

    def generate_random_bits(self, length):
        return random.randrange(2**(length-1)+1, 2**length-1)

    def miller_rabin_test(self, candidate, number_of_rounds):
        pass

    # def generate_key(self):
    #     rand_bits = self.generate_random_bits(1024)
    #     result = self.miller_rabin_test(randbits, 100)
    #     ...jotain...
    #     return jotain
