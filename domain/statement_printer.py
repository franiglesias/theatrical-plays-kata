class StatementPrinter:
    def __init__(self, printer):
        self.printer = printer

    def print(self, invoice):
        self.printer.print(f'Statement for {invoice.customer()}\n')

        self.print_lines(invoice)

        self.printer.print(f'Amount owed is {FormattedAmount(invoice.amount()).dollars()}\n')
        self.printer.print(f'You earned {invoice.credits().current()} credits\n')

        return self.printer.output()

    def print_lines(self, invoice):
        for performance in invoice.performances():
            self.print_details(performance)

    def print_details(self, performance):
        self.printer.print(FormattedPerformance(performance).formatted())


class FormattedPerformance:
    def __init__(self, performance):
        self._performance = performance

    def formatted(self):
        return f' {self._performance.title()}: {FormattedAmount(self._performance.amount()).dollars()} ({self._performance.audience()} seats)\n'


class FormattedAmount:
    def __init__(self, amount):
        self.amount = amount

    def dollars(self):
        return f"${self.amount.current() / 100:0,.2f}"
