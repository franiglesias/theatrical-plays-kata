import math

from domain.amount import Amount
from domain.credits import Credits


class Play:
    def __init__(self, data):
        self._data = data

    def name(self):
        return self._data['name']

    def type(self):
        return self._data['type']

    def calculate_amount_for_comedy(self, audience):
        return Amount(30000) \
            .add(self.extra_amount_for_high_audience_in_comedy(audience)) \
            .add(Amount(300 * audience))

    def extra_amount_for_high_audience_in_comedy(self, audience):
        if audience <= 20:
            return Amount(0)

        return Amount(10000 + 500 * (audience - 20))

    def calculate_amount_for_tragedy(self, audience):
        return Amount(40000) \
            .add(self.extra_amount_for_high_audience_in_tragedy(audience))

    def extra_amount_for_high_audience_in_tragedy(self, audience):
        if audience <= 30:
            return Amount(0)

        return Amount(1000 * (audience - 30))

    def credits(self, audience):
        if "comedy" != self.type():
            return Credits(0)

        return Credits(math.floor(audience / 5))

    def amount(self, audience):
        if self.type() == "tragedy":
            return self.calculate_amount_for_tragedy(audience)
        if self.type() == "comedy":
            return self.calculate_amount_for_comedy(audience)

        raise ValueError(f'unknown type: {self.type()}')


class Plays:
    def __init__(self, data):
        self._data = data

    def get_by_id(self, play_id):
        return Play(self._data[play_id])
