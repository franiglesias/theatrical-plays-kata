import math

from domain.amount import Amount
from domain.credits import Credits


class Performance:
    def __init__(self, perf, plays):
        self._audience = perf['audience']
        self._play_id = perf['playID']
        self._play = plays.get_by_id(self._play_id)
        self._amount = None

    def audience(self):
        return self._audience

    def play(self):
        return self._play

    def calculate_amount_for_comedy(self):
        return Amount(30000) \
            .add(self.extra_amount_for_high_audience_in_comedy()) \
            .add(Amount(300 * self.audience()))

    def extra_amount_for_high_audience_in_comedy(self):
        if self.audience() <= 20:
            return Amount(0)

        return Amount(10000 + 500 * (self.audience() - 20))

    def calculate_amount_for_tragedy(self):
        return Amount(40000) \
            .add(self.extra_amount_for_high_audience_in_tragedy())

    def extra_amount_for_high_audience_in_tragedy(self):
        if self.audience() <= 30:
            return Amount(0)

        return Amount(1000 * (self.audience() - 30))

    def credits(self):
        return Credits(max(self.audience() - 30, 0)). \
            add(self.extra_volume_credits_for_comedy())

    def extra_volume_credits_for_comedy(self):
        if "comedy" != self.play().type():
            return Credits(0)

        return Credits(math.floor(self.audience() / 5))

    def amount(self):
        if self._amount is not None:
            return self._amount

        if self.play().type() == "tragedy":
            tragedy = self.calculate_amount_for_tragedy()
            self._amount = tragedy
            return tragedy
        if self.play().type() == "comedy":
            comedy = self.calculate_amount_for_comedy()
            self._amount = comedy
            return comedy

        raise ValueError(f'unknown type: {self.play().type()}')


class Performances:
    def __init__(self, data, plays):
        self._data = data
        self._plays = plays

    def __iter__(self):
        return PerformancesIterator(self)

    def by_index(self, index):
        return Performance(self._data[index], self._plays)

    def size(self):
        return len(self._data)


class PerformancesIterator:
    def __init__(self, performances):
        self._performances = performances
        self._current = 0

    def __next__(self):
        if self._current >= self._performances.size():
            raise StopIteration

        result = self._performances.by_index(self._current)
        self._current += 1
        return result
