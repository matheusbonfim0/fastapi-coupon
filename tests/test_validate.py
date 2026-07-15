import unittest
from datetime import date, timedelta

from coupons.utils.validate import date_format, expiry_date_greater_than_current_date


class DateValidationTests(unittest.TestCase):
    def test_date_format(self):
        self.assertTrue(date_format('2030-01-31'))
        self.assertFalse(date_format('31/01/2030'))

    def test_expiration_must_be_future(self):
        self.assertTrue(expiry_date_greater_than_current_date(date.today() + timedelta(days=1)))
        self.assertFalse(expiry_date_greater_than_current_date(date.today()))
