class KeyPair:
    """Tämä luokka muodostaa salausavainparin.
    """
    def __init__(self, mod, pub, pri):
        self.__modulus = mod
        self.__public_key_part = pub
        self.__private_key_part = pri

    def get_public_key(self):
        """Tämä funktio palauttaa julkisen avaimen.

        Returns:
            merkkijono: julkinen avain
        """
        public = str(self.__modulus)+str(self.__public_key_part)
        return public

    def get_private_key(self):
        """Tämä funktio palauttaa salaisen avaimen.

        Returns:
            merkkijono: salainen avain
        """
        private = str(self.__modulus)+str(self.__private_key_part)
        return private

    def get_parts(self):
        """Tämä funktio palauttaa ne osa, joista avaimet muodostetaan.

        Returns:
            tuple: avaimen osiot, jotka ovat lukuja (int)
        """
        return self.__modulus, self.__public_key_part, self.__private_key_part
