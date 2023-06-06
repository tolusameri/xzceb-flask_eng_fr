'''#import unittest package'''
import unittest
'''#import translator functions from traslator module'''
from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    '''
    Class to Test translator.py module
    '''

    def test_english_to_french(self):
        '''
        Method to test english to french traslation
        '''
        self.assertEqual(english_to_french('Hi'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hi'), 'Hello')

    def test_french_to_english(self):
        '''
        Method to test english to french traslation
        '''
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Salut')

if __name__ == '__main__':
    unittest.main()

