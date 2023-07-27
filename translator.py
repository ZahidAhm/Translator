 """
 Translator Module
 This module provides functions to translate text between English and French.
 """
# translator.py
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """.............................................
    Translates English text to French.
    Args:
        english_text (str): The text to be translated.
    Returns:
        str: The translated text in French.
        ..........................................
    """
    return MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)

def french_to_english(french_text):
    """.............................................
    Translates French text to English.
    Args:
        english_text (str): The text to be translated.
    Returns:
        str: The translated text in French.
        ..........................................
    """
    return MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)
# Unit Tests
def test_english_to_french(word,test):
    """
    test the conversion function
    """
    result = english_to_french(word)
    if result!=test:
        print("EnglishToFrench - assertNotEqual ")
    else:
        print("EnglishToFrench - assertEqual")
def test_french_to_english(word,test):
    """
    test the conversion function
    """
    result = french_to_english(word)
    if result!=test:
        print("frenchToEnglish - assertNotEqual ")
    else:
        print("frenchToEnglish - assertEqual")
# Run the tests
test_french_to_english("Merci","Thank you")
test_french_to_english("Bonjour","Hi")
test_english_to_french("Hello","Bonjour")
test_english_to_french("Day","Jour")


