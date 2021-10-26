import unittest
from valid_parentheses import isValid


class TestIfValid(unittest.TestCase):
    def test(self):
        test_cases = {'()': True, '((': False, '(){}[][]': True,
                      '{}{}()[[{{}}]])': False}

        for key, val in test_cases.items():
            self.assertEqual(isValid(key), val)
            print(key, val)
