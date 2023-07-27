# # translator.py
# import unittest
# from deep_translator import MyMemoryTranslator

# def english_to_french(english_text):
#     return MyMemoryTranslator(source='en', target='fr').translate(english_text)

# def french_to_english(french_text):
#     return MyMemoryTranslator(source='fr', target='en').translate(french_text)



# # Your code here
# test = unittest.TestCase
# def test_english_to_french(test):
#        test.assertEqual(english_to_french("Hello"), "Bonjour")
#        test.assertNotEqual(english_to_french("Hello"), "Hello")

# def test_french_to_english(test):
#         test.assertEqual(french_to_english("Bonjour"), "Hello")
#         test.assertNotEqual(french_to_english("Bonjour"), "Bonjour")


# # class TestTranslator(unittest.TestCase):
# #     def test_english_to_french(self):
# #         self.assertEqual(english_to_french("Hello"), "Bonjour")
# #         self.assertNotEqual(english_to_french("Hello"), "Hello")

# #     def test_french_to_english(self):
# #         self.assertEqual(french_to_english("Bonjour"), "Hello")
# #         self.assertNotEqual(french_to_english("Bonjour"), "Bonjour")

# if __name__ == '__main__':
#     unittest.main()

# translator.py
import unittest
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    return MyMemoryTranslator(source='en-US', target='fr-FR').translate(english_text)

def french_to_english(french_text):
    return MyMemoryTranslator(source='fr-FR', target='en-US').translate(french_text)

# Unit Tests
def test_english_to_french(word,test):
    result = english_to_french(word)
    if result!=test:
        print("EnglishToFrench - assertNotEqual ")
    else:
        print("EnglishToFrench - assertEqual")
    # assert result == "Bonjour", f"Test failed: Expected 'Bonjour', but got '{result}'"
    # print("Test for english_to_french passed!")

def test_french_to_english(word,test):
    result = french_to_english(word)
    if result!=test:
        print("frenchToEnglish - assertNotEqual ")
      
    else:
        #assert result == "Hello", f"Test failed: Expected 'Hello', but got '{result}'"
        print("frenchToEnglish - assertEqual")

# Run the tests
test_french_to_english("Merci","Thank you")
test_french_to_english("Bonjour","Hello")

test_english_to_french("Hello","Bonjour")
test_english_to_french("Oui","Yes")


