#-*- coding: utf-8 -*-
import unittest
from language_detector import detect_language as dl
from language_detector import *

class TestStringMethods(unittest.TestCase):

    def test_arabic(self):
        text = """
        وجاء في بيان صادر عن مكتب رئيس الحكومة حيدر العبادي إن الخطوة التركية "انتهاك خطير للسيادة العراقية".

        """
        self.assertEqual(dl(text), "Arabic")

    def test_french(self):
        text = """
        Trois assaillants ont été tués et deux autres arrêtés vendredi à Bujumbura après avoir tendu une embuscade à Christophe Manirambona, chef du bureau des unités spécialisées, un haut responsable de la police qui n'était pas dans son véhicule.
        """
        self.assertEqual(dl(text), "French")

    def test_english(self):
        text = """
        JEM Raw is recalling nut butters after health officials found a likely link to a salmonella outbreak. 82 Shares. Email. A salmonella outbreak linked to an organic line of nut butters has sickened 11 people according to the Centers for Disease Control 
        """
        self.assertEqual(dl(text), "English")

    def test_german(self):
        text = """
        "Die unendliche Geschichte" fasziniert Leser, Hörer und Zuschauer seit fast vierzig Jahren. Eine Kinderjury zeichnete nun die klangvolle Neuvertonung des Klassikers als bestes Kinderhörspiel aus.
        """
        self.assertEqual(dl(text), "German")

    def test_kurmanci(self):
        text = """
        Luv xelata xwe pêşkêşî 55 milyon kurd û pêşmergeyan kir Zêdetir
        """
        self.assertEqual(dl(text), "Kurmanci")

    def test_sorani(self):
        text = """
        22:18 | دەمیرتاش: كورد گەیشتووەتە "خاڵێكی مەزن" بۆ راگەیاندنی دەوڵەتی خۆی
        """
        self.assertEqual(dl(text), "Sorani")

    def test_turkish(self):
        text = """
        Amerikan Federal Soruşturma Bürosu (FBI), ABD'nin Kaliforniya Eyaleti'nde Çarşamba günü gerçekleştirilen ve 14 kişinin yaşamını yitirdiği saldırının 'terörizm eylemi' olarak inceleneceğini söyledi.
        """
        self.assertEqual(dl(text), "Turkish")

    def test_english_iterable(self):
        iterable = ["Washington", "Adams", "Jefferson"]
        self.assertEqual(dl(iterable), "English")

    def test_is_english(self):
        text = "Bla bla bla I'm not sure where to start."
        self.assertEqual(isEnglish(text), True)

    def test_return_as_code(self):
        text = "Bla bla bla I'm not sure where to start."
        self.assertEqual(dl(text, return_as_code=True), "en")

    def test_iterable(self):
        iterable = [u'01', u'03', u'04', u'07', u'08', u'10', u'12', u'13', u'16', u'15', u'18', u'11', u'17', u'09', u'06', u'02', u'05', u'14']
        language = detect_language_iterable(iterable)
        self.assertEqual(language, None)

if __name__ == '__main__':
    unittest.main()
