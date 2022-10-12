from domain.amount import Amount
from domain.credits import Credits
from domain.performance import Performances
from domain.play import Plays


class Invoice:
    def __init__(self, data, plays):
        self._data = data
        self._customer = data['customer']
        self._performances = Performances(data['performances'], Plays(plays))

    def _amount(self):
        amount = Amount(0)
        for performance in self._performances:
            amount = amount.add(performance.amount())

        return amount

    def _credits(self):
        volume_credits = Credits(0)
        for performance in self._performances:
            volume_credits = volume_credits.add(performance.credits())

        return volume_credits

    def fill(self, statement_printer):
        for performance in self._performances:
            performance.fill(statement_printer)
        statement_printer.fill('credits', self._credits())
        statement_printer.fill('amount', self._amount())
        statement_printer.fill('customer', self._customer)
