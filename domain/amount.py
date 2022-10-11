class Amount:
    def __init__(self, initial_amount):
        self._amount = initial_amount

    def current(self):
        return self._amount

    def add(self, other):
        return Amount(self._amount + other.current())


class ExtraAmountByAudience:
    def __init__(self):
        self._threshold = 0
        self._minimum_amount = 0
        self._coefficient = 1

    def when_audience_greater_than(self, threshold):
        self._threshold = threshold
        return self

    def minimum_amount_of(self, minimum_amount):
        self._minimum_amount = minimum_amount
        return self

    def and_coefficient(self, coefficient):
        self._coefficient = coefficient
        return self

    def amount(self, audience):
        if audience <= self._threshold:
            return Amount(0)
        return Amount(self._minimum_amount + self._coefficient * (audience - self._threshold))
