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

    def __iter__(self):
        return PerformancesIterator(self)

    def by_index(self, index):
        play = self._data[index]
        return Performance(play['audience'], self._plays.get_by_id(play['playID']))

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
