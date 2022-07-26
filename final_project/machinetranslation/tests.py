import unittest

from translator import english_to_french, french_to_english

class Test(unittest.TestCase):
    def test_frenchToEnglishNull(self):
        self.assertRaises(ValueError,  french_to_english, None)

    def test_englishTofrenchIsNull(self):
        self.assertRaises(ValueError,  english_to_french, None)

    def test_frenchToEnglish(self):
        results = french_to_english('Bonjour')
        self.assertEqual(results["translations"][0]["translation"],'Hello')

    def test_englishToFrench(self):
        results = english_to_french('Hello')
        self.assertEqual(results["translations"][0]["translation"],'Bonjour')

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
