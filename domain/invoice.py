from domain.amount import Amount
from domain.credits import Credits
from domain.performance import Performances
from domain.play import Plays


class Invoice:
    def __init__(self, data, plays):
        self._data = data
        self._customer = data['customer']
        self._performances = Performances(data['performances'], Plays(plays))

    def customer(self):
        return self._customer

    def performances(self):
        return self._performances

    def amount(self):
        amount = Amount(0)
        for performance in self.performances():
            amount = amount.add(performance.amount())

        return amount

    def credits(self):
        volume_credits = Credits(0)
        for performance in self.performances():
            volume_credits = volume_credits.add(performance.credits())

        return volume_credits

    def fill(self, statement_printer):
        statement_printer.fill('customer', self.customer())
        for performance in self.performances():
            statement_printer.fill('line', performance.title(), performance.amount(), performance.audience())
        statement_printer.fill('amount', self.amount())
        statement_printer.fill('credits', self.credits())
