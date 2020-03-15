import unittest

from .string_functions import set_text_to_upper


class StringFunctionsMethods(unittest.TestCase):

    def test_set_text_to_upper(self):
        # Assert results
        self.assertEqual(set_text_to_upper(''), '')
        self.assertEqual(set_text_to_upper('rui'), 'RUI')
        self.assertEqual(set_text_to_upper('nike'), 'NIKE')


if __name__ == '__main__':
    unittest.main()

