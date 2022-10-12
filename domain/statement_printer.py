class StatementPrinter:
    def __init__(self, printer):
        self._printer = printer
        self._customer = None
        self._amount = None
        self._credits = None
        self._lines = []

    def print(self):
        self._printer.print(f'Statement for {self._customer}\n')
        for line in self._lines:
            self._printer.print(f' {line["title"]}: {FormattedAmount(line["amount"]).dollars()} ({line["audience"]} seats)\n')

        self._printer.print(f'Amount owed is {FormattedAmount(self._amount).dollars()}\n')
        self._printer.print(f'You earned {self._credits.current()} credits\n')

        return self._printer.output()

    def fill(self, template, *args):
        getattr(self, '_fill_' + template)(*args)

    def _fill_credits(self, credits):
        self._credits = credits

    def _fill_amount(self, amount):
        self._amount = amount

    def _fill_customer(self, customer):
        self._customer = customer

    def _fill_line(self, title, amount, audience):
        self._lines.append({"title": title, "amount": amount, "audience": audience})


class FormattedAmount:
    def __init__(self, amount):
        self.amount = amount

    def dollars(self):
        return f"${self.amount.current() / 100:0,.2f}"
