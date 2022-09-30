import math

from domain.amount import Amount
from domain.credits import Credits
from domain.play import Play


class Performance:
    def __init__(self, perf, plays):
        self._audience = perf['audience']
        self._play_id = perf['playID']
        self._play = Play(plays[perf['playID']])

    def audience(self):
        return self._audience

    def play_id(self):
        return self._play_id

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
        if self.play().type() == "tragedy":
            return self.calculate_amount_for_tragedy()
        if self.play().type() == "comedy":
            return self.calculate_amount_for_comedy()

        raise ValueError(f'unknown type: {self.play().type()}')
