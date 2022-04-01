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
            tuple: monikko, jossa on julkisen avaimen osiot modulus ja eksponentti,
            jotka ovat lukuja (int)
        """
        public = self.__modulus, self.__public_key_part
        return public

    def get_private_key(self):
        """Tämä funktio palauttaa salaisen avaimen.

        Returns:
            tuple: monikko, jossa on salaisen avaimen osiot modulus ja eksponentti,
            jotka ovat lukuja (int)
        """
        private = self.__modulus, self.__private_key_part
        return private

    def get_all_parts(self):
        """Tämä funktio palauttaa ne osa, joista avaimet muodostetaan.

        Returns:
            tuple: monikko, jossa on kaikki avainparin osiot:
            modulus, julkisen avaimen eksponentti ja salaisen avaimen eksponentti,
            jotka ovat kaikki lukuja (int)
        """
        return self.__modulus, self.__public_key_part, self.__private_key_part
