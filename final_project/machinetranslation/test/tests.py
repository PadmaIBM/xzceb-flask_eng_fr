import unittest
import logging
import sys
from translator import english_to_french, french_to_english

class TestTranslationMethods(unittest.TestCase):

    def test_english_to_french(self):
        print("Testing Hello==Bonjour , Errors:",self.assertEqual(english_to_french("Hello"), "Bonjour"))
        print("Testing Hello!=Comment vuos etes , Errors:",self.assertNotEqual(english_to_french("Hello"),"Comment vuos etes"))

    def test_french_to_english(self):
        print("Testing Bonjour==Hello , Errors:", self.assertEqual(french_to_english("Bonjour"),"Hello"))
        print("Testing Bonjour!=How are you , Errors:",self.assertNotEqual(french_to_english("Bonjour"),"How are you"))

if __name__ == "__main__":
    logging.basicConfig( stream=sys.stderr )
    logging.getLogger( "SomeTest.testSomething" ).setLevel( logging.DEBUG )
    unittest.main()