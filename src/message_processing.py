
class MessageProcessing:
    """Tämä luokka sisältää toiminnot viestin salaamista ja
    salauksen purkamista varten."""
    def __init__(self):
        pass

    def message_to_int(self, message):
        """Tämä funktio muuttaa viestin binäärimuotoon.

        Args:
            message (string): viesti merkkijonona

        Returns:
            string: viesti binäärimuodossa merkkijonona
        """
        message_as_byte = message.encode(encoding='utf_8')
        message_as_int = int.from_bytes(message_as_byte, "big")
        return message_as_int

    def message_to_string(self, message_as_int):
        """Tämä funktio muuttaa binäärimuodossa olevan viestin
        tekstimuotoiseksi.

        Args:
            message_as_bin (binääri): viesti binäärilukuna

        Returns:
            string: viesti merkkijonona luettavassa muodossa
        """
        length_in_bytes = (message_as_int.bit_length() + 7) // 8
        message_as_byte = message_as_int.to_bytes(length_in_bytes, "big")
        try:
            message_as_string = message_as_byte.decode('utf_8')
        except UnicodeDecodeError:
            return "Jotain meni pieleen. Salausavain tai viesti oli virheellinen."
        return message_as_string

    def encrypt_message(self, message, public_key_part, modulus):
        """Tämä funktio salaa viestin.

        Args:
            message (string): salattava viesti
            public_key_part (int): julkisen avaimen eksponenttiosa
            modulus (int): salausavaimen modulusosa

        Returns:
            int: salattu viesti
        """
        message_as_int = self.message_to_int(message)
        encrypted_message = pow(message_as_int, public_key_part, modulus)
        return encrypted_message

    def decrypt_message(self, encrypted_message, private_key_part, modulus):
        """Tämä funktio purkaa salatun viestin.

        Args:
            encrypted_message (int): salattu viesti
            private_key_part (int): yksityisen avaimen eksponenttiosa
            modulus (int): salausavaimen modulusosa

        Returns:
            string: purettu viesti merkkijonona luettavassa muodossa
        """
        message_as_int = pow(encrypted_message, private_key_part, modulus)
        decrypted_message = self.message_to_string(message_as_int)
        return decrypted_message
