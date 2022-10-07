from domain.invoice import Invoice
from domain.printer import Printer


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


def statement(invoice_data, plays):
    invoice = Invoice(invoice_data, plays)

    printer = Printer()
    printer.print(f'Statement for {invoice.customer()}\n')

    for performance in invoice.performances():
        line = Line(performance.title(), performance.audience(), performance.amount())
        printer.print(line.formatted())

    printer.print(f'Amount owed is {FormattedAmount(invoice.amount()).dollars()}\n')
    printer.print(f'You earned {invoice.credits().current()} credits\n')

    return printer.output()
