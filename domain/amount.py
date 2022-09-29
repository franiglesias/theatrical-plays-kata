class Amount:
    def __init__(self, initial_amount):
        self._amount = initial_amount

    def current(self):
        return self._amount

    def add(self, other):
        new_amount = self._amount + other.current()
        return Amount(new_amount)
