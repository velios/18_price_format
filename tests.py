import unittest

from format_price import format_price


class FormatPriceTestCase(unittest.TestCase):
    def test_is_result_string_type(self):
        self.assertIsInstance(
            format_price('1234.1234'),
            str,
        )

    def test_is_correct_formatted(self):
        self.assertEqual(
            format_price('123456789.12345'),
            '123 456 789.12',
        )

    def test_is_correct_error_value_processing(self):
        self.assertIsNone(
            format_price('qwerty'),
        )

    def test_negative_number(self):
        self.assertEqual(
            format_price('-123456789.12'),
            '-123 456 789.12'
        )

    def test_with_plus_number(self):
        self.assertEqual(
            format_price('+123456789.12'),
            '123 456 789.12'
        )

    def test_with_comma_number(self):
        self.assertEqual(
            format_price('1234,1234'),
            '1 234.12'
        )


if __name__ == '__main__':
    unittest.main()
