class MutableTuple:
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    # Return the key of the tuple
    def key(self):
        return self.__key

    # Return the value of the tuple
    def value(self):
        return self.__value

    # Comparision operator
    def __lt__(self, other):
        return self.value() < other.value()

    # String operator override
    def __str__(self):
        return "<" + str(self.key()) + ", " + str(self.value()) + ">"