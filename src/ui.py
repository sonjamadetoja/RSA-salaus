from keycreationmachine import KeyCreationMachine
from message_processing import MessageProcessing

class UI:
    """Tämä luokka muodostaa käyttöliittymän."""
    def __init__(self):
        self.machine = KeyCreationMachine()
        self.processing = MessageProcessing()

    def menu_view(self):
        while True:
            print("Valitse toiminto numerolla:")
            print("1 Luo salausavainpari")
            print("2 Salaa viesti")
            print("3 Pura viestin salaus")
            print("4 Lopeta")
            choice = input("Valintani: ")
            if choice == "1":
                self.generate()
            elif choice == "2":
                self.encrypt()
            elif choice == "3":
                self.decrypt()
            elif choice == "4":
                print("Ohjelma päättyy.")
                break
            else:
                print("Virheellinen valinta.")

    def generate(self):
        key_pair = self.machine.generate_key_pair()
        parts = key_pair.get_all_parts()
        modulus = parts[0]
        public_part = parts[1]
        private_part = parts[2]
        print("modulus: ", modulus)
        print("julkinen osa: ", public_part)
        print("yksityinen osa: ", private_part)

    def encrypt(self):
        message = input("Anna salattava viesti: ")
        modulus = int(input("Anna salausavaimen modulus-osa: "))
        public_part = int(input("Anna salausavaimen julkinen osa: "))
        encrypted_message = self.processing.encrypt_message(message, public_part, modulus)
        print(encrypted_message)

    def decrypt(self):
        message = int(input("Anna salattu viesti: "))
        modulus = int(input("Anna salausavaimen modulus-osa: "))
        private_part = int(input("Anna salausavaimen yksityinen osa: "))
        decrypted_message = self.processing.decrypt_message(message, private_part, modulus)
        print(decrypted_message)
