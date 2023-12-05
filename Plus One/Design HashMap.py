class MyHashMap:
    def __init__(self):
        self.map = []

    def put(self, key, value):
        for pair in self.map:
            if pair[0] == key:
                pair[1] = value
                return
        self.map.append([key, value])

    def get(self, key):
        for pair in self.map:
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key):
        for pair in self.map:
            if pair[0] == key:
                self.map.remove(pair)
                return
