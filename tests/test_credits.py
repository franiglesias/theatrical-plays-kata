import unittest

from domain.credits import Credits


class CreditsTestCase(unittest.TestCase):
    def test_contains_credits(self):
        self.assertEqual(100, Credits(100).current())  # add assertion here

    def test_accumulates_credits(self):
        initial_credits = Credits(100)
        extra = Credits(100)
        self.assertEqual(200, initial_credits.add(extra).current())


if __name__ == '__main__':
    unittest.main()
