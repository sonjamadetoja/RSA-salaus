
class MessageProcessing:
    """Tämä luokka sisältää toiminnot viestin salaamista ja
    salauksen purkamista varten."""
    def __init__(self):
        pass

    def message_to_bin(self, message):
        """Tämä funktio muuttaa viestin binäärimuotoon.

        Args:
            message (string): viesti merkkijonona

        Returns:
            string: viesti binäärimuodossa merkkijonona
        """
        message_as_byte = message.encode(encoding='utf_8')
        message_as_hex = message_as_byte.hex()
        message_as_int = int(message_as_hex, 16)
        message_as_bin = bin(message_as_int)
        message_as_bin = message_as_bin.lstrip('0b')
        return message_as_bin

    def message_to_string(self, message_as_bin):
        message_as_int = int(str(message_as_bin), 2)
        message_as_hex = hex(message_as_int).lstrip('0x')
        message_as_byte = bytes.fromhex(message_as_hex)
        message_as_string = message_as_byte.decode('utf_8')
        return message_as_string

    def encrypt_message(self, message, public_key_part, modulus):
        message_as_bin = self.message_to_bin(message)
        message_as_bin = int(message_as_bin)
        encrypted_message = pow(message_as_bin, public_key_part, modulus)
        return encrypted_message

    def decrypt_message(self, encrypted_message, private_key_part, modulus):
        message_as_bin = pow(encrypted_message, private_key_part, modulus)
        decrypted_message = self.message_to_string(message_as_bin)
        return decrypted_message
