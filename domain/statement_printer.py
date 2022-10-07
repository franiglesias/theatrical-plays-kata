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
        line = Line(performance.title(), performance.audience(), performance.amount())
        self.printer.print(line.formatted())


class Line:
    def __init__(self, title, audience, amount):
        self.title = title
        self.audience = audience
        self.amount = amount

    def formatted(self):
        return f' {self.title}: {FormattedAmount(self.amount).dollars()} ({self.audience} seats)\n'


class FormattedAmount:
    def __init__(self, amount):
        self.amount = amount

    def dollars(self):
        return f"${self.amount.current() / 100:0,.2f}"
