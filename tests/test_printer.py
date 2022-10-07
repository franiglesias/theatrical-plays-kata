import unittest

from infrastructure.console_printer import ConsolePrinter


class PrinterTestCase(unittest.TestCase):
    def test_can_print_lines(self):
        printer = ConsolePrinter()

        printer.print("Line 1")
        printer.print("Line 2")

        expected = "Line 1Line 2"

        self.assertEqual(expected, printer.output())


if __name__ == '__main__':
    unittest.main()
