class Play:
    def __init__(self, data):
        self._data = data

    def name(self):
        return self._data['name']

    def type(self):
        return self._data['type']


class Plays:
    def __init__(self, data):
        self._data = data

    def get_by_id(self, play_id):
        return Play(self._data[play_id])
