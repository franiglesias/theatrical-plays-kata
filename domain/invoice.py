from domain.performance import Performances
from domain.play import Plays


class Invoice:
    def __init__(self, data, plays):
        self._data = data
        self._customer = data['customer']
        self._performances = Performances(data['performances'], Plays(plays))

    def _amount(self):
        return self._performances.amount()

    def _credits(self):
        return self._performances.credits()

    def fill(self, statement_printer):
        statement_printer.fill('credits', self._credits())
        statement_printer.fill('amount', self._amount())
        statement_printer.fill('customer', self._customer)
        self._performances.fill(statement_printer)
