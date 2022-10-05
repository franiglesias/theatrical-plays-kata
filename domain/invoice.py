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
        invoice_amount = Amount(0)
        for performance in self.performances():
            invoice_amount = invoice_amount.add(performance.amount())

        return invoice_amount

    def credits(self):
        volume_credits = Credits(0)
        for performance in self.performances():
            volume_credits = volume_credits.add(performance.credits())

        return volume_credits
