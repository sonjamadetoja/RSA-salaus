from keycreationmachine import KeyCreationMachine

KCM = KeyCreationMachine()

random_bits = KCM.generate_random_bits(1024)

print(random_bits)
