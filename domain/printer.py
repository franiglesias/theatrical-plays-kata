class Printer:
    def __init__(self):
        self._lines = ""

    def print(self, line):
        self._lines += line

    def output(self):
        return self._lines
