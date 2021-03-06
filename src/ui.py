from keycreationmachine import KeyCreationMachine
from message_processing import MessageProcessing

class UI:
    """Tämä luokka muodostaa käyttöliittymän."""
    def __init__(self):
        self.machine = KeyCreationMachine()
        self.processing = MessageProcessing()
        self._newest_key = None

    def menu_view(self):
        print("*********RSA-salausohjelma*********")
        while True:
            print("Valitse toiminto numerolla:")
            print("1 Luo salausavainpari")
            print("2 Salaa viesti")
            print("3 Pura viestin salaus")
            print("4 Poista viimeksi luotu avain muistista")
            print("5 Lopeta")
            choice = input("Valintani: ")
            if choice == "1":
                self.generate()
            elif choice == "2":
                self.encrypt()
            elif choice == "3":
                self.decrypt()
            elif choice == "4":
                self._newest_key = None
            elif choice == "5":
                print("Ohjelma päättyy.")
                print("***********************************")
                break
            else:
                print("Virheellinen valinta.")

    def generate(self):
        key_pair = self.machine.generate_key_pair()
        parts = key_pair.get_all_parts()
        modulus = parts[0]
        public_part = parts[1]
        private_part = parts[2]
        self._newest_key = parts
        print("modulus: ", modulus)
        print("julkinen osa: ", public_part)
        print("yksityinen osa: ", private_part)
        while True:
            save_file = input("Haluatko tallentaa avainparin tiedostoon (kyllä/ei)? ")
            if save_file == "kyllä":
                data = f"""modulus: {modulus}
julkinen osa: {public_part}
yksityinen osa: {private_part}"""
                try:
                    self.save_to_file("RSA_avain.txt", data)
                except FileExistsError:
                    name_string = "RSA_avain"+str(modulus)[0:5]+".txt"
                    self.save_to_file(name_string, data)
                break
            if save_file == "ei":
                break
            else:
                print("Virheellinen syöte")

    def save_to_file(self, name, data):
        with open(name, "x") as file:
            print("Tallennetaan...")
            file.write(data)
            print(name)
            print("Valmis!")

    def encrypt(self):
        while True:
            message = input("Anna salattava viesti: ")
            if len(message) <= 256:
                break
            print("""Viesti on liian pitkä. Salattavan viestin
            pituus voi olla korkeintaan 256 bittiä.""")
        while True:
            reply = "ei"
            if self._newest_key is not None:
                reply = input("Käytä viimeksi luotua avainta (kyllä/ei): ")
            if reply == "kyllä":
                modulus = self._newest_key[0]
                public_part = self._newest_key[1]
                break
            if reply == "ei":
                modulus, public_part = self._ask_for_public_key()
                break
            else:
                print("Virheellinen syöte")
        encrypted_message = self.processing.encrypt_message(message, public_part, modulus)
        print("Viesti salattuna:")
        print(encrypted_message)
        print("-----")

    def _ask_for_public_key(self):
        while True:
            try:
                modulus = int(input("Anna salausavaimen modulus-osa: "))
                break
            except ValueError:
                print("Virheellinen syöte")
        while True:
            try:
                public_part = int(input("Anna salausavaimen julkinen osa: "))
                break
            except ValueError:
                print("Virheellinen syöte")
        return modulus, public_part

    def decrypt(self):
        while True:
            try:
                message = int(input("Anna salattu viesti: "))
                break
            except ValueError:
                print("Virheellinen syöte")
        while True:
            reply = "ei"
            if self._newest_key is not None:
                reply = input("Käytä viimeksi luotua avainta (kyllä/ei): ")
            if reply == "kyllä":
                modulus = self._newest_key[0]
                private_part = self._newest_key[2]
                break
            if reply == "ei":
                modulus, private_part = self._ask_for_private_key()
                break
            else:
                print("Virheellinen syöte")
        decrypted_message = self.processing.decrypt_message(message, private_part, modulus)
        error_message = "Jotain meni pieleen. Salausavain tai viesti oli virheellinen."
        if decrypted_message != error_message:
            print("Viesti purettuna:")
        print(decrypted_message)
        print("-----")

    def _ask_for_private_key(self):
        while True:
            try:
                modulus = int(input("Anna salausavaimen modulus-osa: "))
                break
            except ValueError:
                print("Virheellinen syöte")
        while True:
            try:
                private_part = int(input("Anna salausavaimen yksityinen osa: "))
                break
            except ValueError:
                print("Virheellinen syöte")
        return modulus, private_part
