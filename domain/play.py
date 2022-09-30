class Play:
    def __init__(self, data):
        self._data = data

    def name(self):
        return self._data['name']

    def type(self):
        return self._data['type']
