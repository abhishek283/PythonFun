# -*- coding: utf-8 -*-
'''
   It demonstrates unit test using currency_converter class
'''
import unittest
from currency_converter import CurrencyConverter

class CurrencyConverterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        success=CurrencyConverter().add_country('India',60,'₹')

    def setUp(self):
        print('Run before each method')

    def test_converted_amount(self):
        success, result = CurrencyConverter().converted_amount('India', 25)
        self.assertTrue(success)
        self.assertEquals(result, '1500₹','Currency conversion is incorrect')
        self.assertEquals(result, '1584.25₹','Currency conversion is incorrect')

    def test_changerate(self):
        self.assertTrue(CurrencyConverter().change_rate('India',63.37))
        success, result = CurrencyConverter().converted_amount('India', 25)
        self.assertTrue(success)
        self.assertNotEqual(result, '1500₹')
        self.assertEquals(result, '1584.25₹')

    def test_get_currency_rate(self):
        success, result = CurrencyConverter().get_currency_rate('India')
        self.assertTrue(success)
        self.assertEquals(result, '63.37₹', 'Currency conversion is incorrect')

    def tearDown(self):
        print('Run After each method')

    @classmethod
    def tearDownClass(cls):
        print("I will run after all tests completed")

if __name__ == '__main__':
    unittest.main(verbosity=2)