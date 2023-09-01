from unittest import TestCase
from app import app
from functions import check_invalidity, get_currency_codes




class ForexConverterTestCase(TestCase):

    def setUp(self):
        app.config['TESTING'] = True



    def tests_show_currency_converter(self):
        """should show the forex-converter.html page with currency converter form"""

        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1 class="display-3 text-center mb-5">Forex Currency Converter</h1>', html)



    def tests_get_currency_codes(self):
        self.assertIn('USD', get_currency_codes())
        self.assertIn('EUR', get_currency_codes())
        self.assertIn('COP', get_currency_codes())



    def tests_check_invalidity(self):
        """should show correct message for invalid form submission"""

        self.assertEqual(check_invalidity('hi', 'eur', 5), '"hi" is an invalid currency code')
        self.assertEqual(check_invalidity('usd', 'woah', 5), '"woah" is an invalid currency code')
        self.assertEqual(check_invalidity('', '', ''), 'Please fill out all fields')
        self.assertEqual(check_invalidity('hi', 'woah', 10), '"hi" and "woah" are invalid currency codes')



    def tests_show_conversion(self):
        """should show the conversion rate with the correct currency symbol"""

        with app.test_client() as client:
            res = client.get('/conversion?start-curr=usd&end-curr=usd&amount=1')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<p class="p-2 d-inline mt-5">$ 1</p>', html)