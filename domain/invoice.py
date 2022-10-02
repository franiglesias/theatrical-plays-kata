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
