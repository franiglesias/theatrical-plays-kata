import unittest

from domain.amount import Amount


class AmountTestCase(unittest.TestCase):
    def test_contains_amount(self):
        amount_of_300 = Amount(300)
        self.assertEqual(300, amount_of_300.current())

    def test_can_accumulate_partial_amounts(self):
        amount_of_300 = Amount(300)
        amount_of_500 = amount_of_300.add(Amount(200))
        self.assertEqual(500, amount_of_500.current())


if __name__ == '__main__':
    unittest.main()
