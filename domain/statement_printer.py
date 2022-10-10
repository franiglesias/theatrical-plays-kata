class StatementPrinter:
    def __init__(self, printer):
        self.printer = printer

    def print(self, invoice):
        invoice.fill(self)

        return self.printer.output()

    def fill(self, template, *args):
        getattr(self, 'fill_' + template)(*args)

    def fill_credits(self, credits):
        self.printer.print(f'You earned {credits.current()} credits\n')

    def fill_amount(self, amount):
        self.printer.print(f'Amount owed is {FormattedAmount(amount).dollars()}\n')

    def fill_customer(self, customer):
        self.printer.print(f'Statement for {customer}\n')

    def fill_line(self, title, amount, audience):
        self.printer.print(f' {title}: {FormattedAmount(amount).dollars()} ({audience} seats)\n')


class FormattedAmount:
    def __init__(self, amount):
        self.amount = amount

    def dollars(self):
        return f"${self.amount.current() / 100:0,.2f}"
