import math

from domain.amount import Amount
from domain.audience import Audience
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
        self.minimum_amount = 0
        self.threshold = 30
        self.coefficient = 1000

    def name(self):
        return self._name

    def credits(self, audience):
        return Credits(0)

    def amount(self, audience):
        return Amount(40000).add(Audience(audience).amount(self.threshold, self.minimum_amount, self.coefficient))


class Comedy(Play):
    def __init__(self, data):
        self._name = data['name']
        self.threshold = 20
        self.minimum_amount = 10000
        self.coefficient = 500

    def name(self):
        return self._name

    def credits(self, audience):
        return Credits(math.floor(audience / 5))

    def amount(self, audience):
        return Amount(30000) \
            .add(Audience(audience).amount(self.threshold, self.minimum_amount, self.coefficient)) \
            .add(Amount(300 * audience))


class Plays:
    def __init__(self, data):
        self._data = data

    def get_by_id(self, play_id):
        return Play.create(self._data[play_id])
