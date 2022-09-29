class Credits:

    def __init__(self, initial_credits):
        self._credits = initial_credits

    def current(self):
        return self._credits

    def add(self, more_credits):
        return Credits(self._credits + more_credits.current())
