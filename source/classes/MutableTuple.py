class MutableTuple:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def key(self):
        return self.__key

    def value(self):
        return self.__value

    def __lt__(self, other):
        return self.value() < other.value()

    def __str__(self):
        return "<" + str(self.key()) + ", " + str(self.value()) + ">"