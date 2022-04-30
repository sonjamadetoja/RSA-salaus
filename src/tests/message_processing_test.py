import random
import string
import unittest
from message_processing import MessageProcessing
ticket = random.SystemRandom()

class TestKeyCreationMachine(unittest.TestCase):
    def setUp(self):
        self.MP = MessageProcessing()
        self.characters = string.ascii_letters + " !#¤%&/()=?*;:,.@£$€{[]}+~^'-_–0123456789"

    def test_message_to_int(self):
        message = "hello world"
        mes_int = self.MP.message_to_int(message)
        should_be = 126207244316550804821666916

        self.assertEqual(mes_int, should_be)

    def test_message_to_string(self):
        message_as_int = 126207244316550804821666916
        mes_str = self.MP.message_to_string(message_as_int)
        should_be = "hello world"

        self.assertEqual(mes_str, should_be)

    def test_encrypt_and_decrypt_returns_original_message_256_bits(self):
        original_message = """Se kysymyksen on pyyhkimaan se liikkeelle ja kirmaissut tyttarenne. Ja et omaa syva he jo joko. Se ja vieras se toiset hiukan he. Eri puhuu enhan suopi ensin terve nyt kun hokee jai. Minka me suusi te minun saali. Kullakin kaivanut punainen kuuluvat ja par"""

        enc_mes = self.MP.encrypt_message(
            original_message, 65537,
            13085524541576278595343007039035604940683434979355494944130641516574628345330481201261922833936110002204041766417728895329987322421713635381443005617367601735572629156525157610177700862483891163824069064734198879806356006870886717783241842363222453195496584847348076370497959167974060962500137529535940790377106546528250197162341729800484342346465872839845102139828929576326500284857653585790682720974485843132270636982106136419810211316699786191764858088229824893219232388148694865717671990885868642181066666314616465500126097254192376553155720070748426557558485375040045300253141086151658707110555338522151013689781
            )

        new_message = self.MP.decrypt_message(enc_mes, 1088280688982735042554847793860926876866427550162154587377879084884721787634828994117492567654435930344891124828109790560997541859705970209905169631161971302618957462466093528148581084745539905525475509061045684031685054479908571574493181894208523141768072015967631875999803568137733177840105583177985645939685002811165137252122386228842864685156058374979545175425746202992965704555497433449910423212328203266602728873877198885658714651875889115662843849742758575984961233691260758915833953512474954844048298196434880498260510677983497026495044151911305651951180675010690748736193616062833296719665615064677806586161,
        13085524541576278595343007039035604940683434979355494944130641516574628345330481201261922833936110002204041766417728895329987322421713635381443005617367601735572629156525157610177700862483891163824069064734198879806356006870886717783241842363222453195496584847348076370497959167974060962500137529535940790377106546528250197162341729800484342346465872839845102139828929576326500284857653585790682720974485843132270636982106136419810211316699786191764858088229824893219232388148694865717671990885868642181066666314616465500126097254192376553155720070748426557558485375040045300253141086151658707110555338522151013689781)

        self.assertEqual(new_message, original_message)

    def test_encrypt_and_decrypt_returns_original_message_random_length_short(self):
        original_message = ""
        message_length = ticket.randint(1, 128)
        for _ in range(message_length):
            letter = ticket.choice(self.characters)
            original_message += letter
        print(original_message)
        enc_mes = self.MP.encrypt_message(
            original_message, 65537,
            13085524541576278595343007039035604940683434979355494944130641516574628345330481201261922833936110002204041766417728895329987322421713635381443005617367601735572629156525157610177700862483891163824069064734198879806356006870886717783241842363222453195496584847348076370497959167974060962500137529535940790377106546528250197162341729800484342346465872839845102139828929576326500284857653585790682720974485843132270636982106136419810211316699786191764858088229824893219232388148694865717671990885868642181066666314616465500126097254192376553155720070748426557558485375040045300253141086151658707110555338522151013689781
            )

        new_message = self.MP.decrypt_message(enc_mes, 1088280688982735042554847793860926876866427550162154587377879084884721787634828994117492567654435930344891124828109790560997541859705970209905169631161971302618957462466093528148581084745539905525475509061045684031685054479908571574493181894208523141768072015967631875999803568137733177840105583177985645939685002811165137252122386228842864685156058374979545175425746202992965704555497433449910423212328203266602728873877198885658714651875889115662843849742758575984961233691260758915833953512474954844048298196434880498260510677983497026495044151911305651951180675010690748736193616062833296719665615064677806586161,
        13085524541576278595343007039035604940683434979355494944130641516574628345330481201261922833936110002204041766417728895329987322421713635381443005617367601735572629156525157610177700862483891163824069064734198879806356006870886717783241842363222453195496584847348076370497959167974060962500137529535940790377106546528250197162341729800484342346465872839845102139828929576326500284857653585790682720974485843132270636982106136419810211316699786191764858088229824893219232388148694865717671990885868642181066666314616465500126097254192376553155720070748426557558485375040045300253141086151658707110555338522151013689781)

        self.assertEqual(new_message, original_message)

    def test_encrypt_and_decrypt_returns_original_message_random_length_long(self):
        original_message = ""
        message_length = ticket.randint(129, 256)
        for _ in range(message_length):
            letter = ticket.choice(self.characters)
            original_message += letter
        print(original_message)
        enc_mes = self.MP.encrypt_message(
            original_message, 65537,
            13085524541576278595343007039035604940683434979355494944130641516574628345330481201261922833936110002204041766417728895329987322421713635381443005617367601735572629156525157610177700862483891163824069064734198879806356006870886717783241842363222453195496584847348076370497959167974060962500137529535940790377106546528250197162341729800484342346465872839845102139828929576326500284857653585790682720974485843132270636982106136419810211316699786191764858088229824893219232388148694865717671990885868642181066666314616465500126097254192376553155720070748426557558485375040045300253141086151658707110555338522151013689781
            )

        new_message = self.MP.decrypt_message(enc_mes, 1088280688982735042554847793860926876866427550162154587377879084884721787634828994117492567654435930344891124828109790560997541859705970209905169631161971302618957462466093528148581084745539905525475509061045684031685054479908571574493181894208523141768072015967631875999803568137733177840105583177985645939685002811165137252122386228842864685156058374979545175425746202992965704555497433449910423212328203266602728873877198885658714651875889115662843849742758575984961233691260758915833953512474954844048298196434880498260510677983497026495044151911305651951180675010690748736193616062833296719665615064677806586161,
        13085524541576278595343007039035604940683434979355494944130641516574628345330481201261922833936110002204041766417728895329987322421713635381443005617367601735572629156525157610177700862483891163824069064734198879806356006870886717783241842363222453195496584847348076370497959167974060962500137529535940790377106546528250197162341729800484342346465872839845102139828929576326500284857653585790682720974485843132270636982106136419810211316699786191764858088229824893219232388148694865717671990885868642181066666314616465500126097254192376553155720070748426557558485375040045300253141086151658707110555338522151013689781)

        self.assertEqual(new_message, original_message)
