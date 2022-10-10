import math

from domain.amount import Amount
from domain.credits import Credits


class Play:
    @staticmethod
    def create(data):
        if data['type'] == "tragedy":
            return Tragedy(data)
        if data['type'] == "comedy":
            return Comedy(data)

        raise ValueError(f'unknown type: {data["type"]}')

    def credits(self, audience):
        pass

    def amount(self, audience):
        pass


class Tragedy(Play):
    def __init__(self, data):
        self._name = data['name']

    def name(self):
        return self._name

    def extra_amount_for_high_audience(self, audience):
        if audience <= 30:
            return Amount(0)

        return Amount(1000 * (audience - 30))

    def credits(self, audience):
        return Credits(0)

    def amount(self, audience):
        return Amount(40000).add(self.extra_amount_for_high_audience(audience))


class Comedy(Play):
    def __init__(self, data):
        self._name = data['name']

    def name(self):
        return self._name

    def extra_amount_for_high_audience(self, audience):
        if audience <= 20:
            return Amount(0)

        return Amount(10000 + 500 * (audience - 20))

    def credits(self, audience):
        return Credits(math.floor(audience / 5))

    def amount(self, audience):
        return Amount(30000) \
            .add(self.extra_amount_for_high_audience(audience)) \
            .add(Amount(300 * audience))


class Plays:
    def __init__(self, data):
        self._data = data

    def get_by_id(self, play_id):
        return Play.create(self._data[play_id])
