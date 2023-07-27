# test_translator.py
import unittest
from translator import test_english_to_french,test_french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
        test_english_to_french()

    def test_french_to_english(self):
        test_french_to_english()

if __name__ == '__main__':
    unittest.main()
