from domain.amount import Amount
from domain.credits import Credits


class Performance:
    def __init__(self, audience, play):
        self._audience = audience
        self._play = play
        self._amount = None

    def audience(self):
        return self._audience

    def title(self):
        return self._play.name()

    def credits(self):
        return Credits(max(self.audience() - 30, 0)). \
            add(self._play.credits(self.audience()))

    def amount(self):
        if self._amount is not None:
            return self._amount

        self._amount = self._play.amount(self.audience())

        return self._amount

    def fill(self, statement_printer):
        statement_printer.fill('line', self.title(), self.amount(), self.audience())


class Performances:
    def __init__(self, data, plays):
        self._data = data
        self._plays = plays

    def amount(self):
        amount = Amount(0)
        for data in self._data:
            performance = self._performance(data)
            amount = amount.add(performance.amount())

        return amount

    def _performance(self, data):
        return Performance(data['audience'], self._plays.get_by_id(data['playID']))

    def credits(self):
        volume_credits = Credits(0)
        for data in self._data:
            performance = self._performance(data)
            volume_credits = volume_credits.add(performance.credits())

        return volume_credits

    def fill(self, statement_printer):
        for data in self._data:
            performance = self._performance(data)
            performance.fill(statement_printer)
