import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def setUp(self):
        self.normal_test_value = '123456789.000'
        self.error_test_value = 'qwerty'

    def test_is_result_string_type(self):
        self.assertIsInstance(
            format_price(self.normal_test_value),
            str,
        )

    def test_is_correct_formatted(self):
        self.assertEqual(
            format_price(self.normal_test_value),
            '123 456 789.00',
        )

    def test_is_correct_error_value_processing(self):
        self.assertIsNone(
            format_price(self.error_test_value),
        )


if __name__ == '__main__':
    unittest.main()
