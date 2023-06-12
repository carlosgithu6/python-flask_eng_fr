'''aaa'''
import unittest
from translator import english_to_french, french_to_english

class TestEnglishToFrench(unittest.TestCase):
    '''aaa'''
    def test_english_2_french(self):
        '''aaa'''
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class TestFrenchToEnglish(unittest.TestCase):
    '''aaa'''
    def test_french_2_fnglish(self):
        '''aaa'''
        self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()
