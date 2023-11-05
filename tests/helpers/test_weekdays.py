import datetime
import unittest

from helpers.weekdays import CURRENT_DATE, WEEKDAYS


class TestDateTimeModule(unittest.TestCase):
    def test_weekdays(self):
        expected_weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.assertEqual(WEEKDAYS, expected_weekdays)

    def test_current_date(self):
        current_date = datetime.today().date()
        self.assertEqual(CURRENT_DATE, current_date)

if __name__ == '__main__':
    unittest.main()