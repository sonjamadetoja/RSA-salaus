from keycreationmachine import KeyCreationMachine

KCM = KeyCreationMachine()

print("testi")
x = KCM.generate_key_pair()
print(type(x))
print(x.get_private_key())
print(x.get_public_key())
print(x.get_all_parts())
