import unittest

from translator import englishToFrench, frenchToEnglish

class Test(unittest.TestCase):
    def test_frenchToEnglishNull(self):
        self.assertRaises(ValueError,  frenchToEnglish, None)

    def test_englishTofrenchIsNull(self):
        self.assertRaises(ValueError,  englishToFrench, None)

    def test_frenchToEnglish(self):
        results = frenchToEnglish('Bonjour')
        self.assertEqual(results["translations"][0]["translation"],'Hello')

    def test_englishToFrench(self):
        results = englishToFrench('Hello')
        self.assertEqual(results["translations"][0]["translation"],'Bonjour')

if __name__ == '__main__':
    # begin the unittest.main()
    unittest.main()
