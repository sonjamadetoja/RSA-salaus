class KeyPair:
    def __init__(self, mod, pub, pri):
        self.__modulus = mod
        self.__public_key_part = pub
        self.__private_key_part = pri

    def get_keys(self):
        public = str(self.__modulus)+str(self.__public_key_part)
        private = str(self.__modulus)+str(self.__private_key_part)
        return public, private

    def get_parts(self):
        return self.__modulus, self.__public_key_part, self.__private_key_part
