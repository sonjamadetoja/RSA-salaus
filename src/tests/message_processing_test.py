from email import message
import unittest
from message_processing import MessageProcessing

class TestKeyCreationMachine(unittest.TestCase):
    def setUp(self):
        self.MP = MessageProcessing()

    def test_message_to_bin(self):
        message = "hello world"
        mes_bin = self.MP.message_to_bin(message)
        should_be = "110100001100101011011000110110001101111001000000111011101101111011100100110110001100100"

        self.assertEqual(mes_bin, should_be)

    def test_message_to_string(self):
        message = 110100001100101011011000110110001101111001000000111011101101111011100100110110001100100
        mes_str = self.MP.message_to_string(message)
        should_be = "hello world"

        self.assertEqual(mes_str, should_be)