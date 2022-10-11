import math

from domain.amount import Amount, ExtraAmountByAudience
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

    def credits(self, audience):
        return Credits(0)

    def amount(self, audience):
        calculator = ExtraAmountByAudience(). \
            when_audience_greater_than(30). \
            minimum_amount_of(0). \
            and_coefficient(1000)
        return Amount(40000).add(calculator.amount(audience))


class Comedy(Play):
    def __init__(self, data):
        self._name = data['name']

    def name(self):
        return self._name

    def credits(self, audience):
        return Credits(math.floor(audience / 5))

    def amount(self, audience):
        calculator = ExtraAmountByAudience(). \
            when_audience_greater_than(20). \
            minimum_amount_of(10000). \
            and_coefficient(500)

        return Amount(30000) \
            .add(calculator.amount(audience)) \
            .add(Amount(300 * audience))


class Plays:
    def __init__(self, data):
        self._data = data

    def get_by_id(self, play_id):
        return Play.create(self._data[play_id])
