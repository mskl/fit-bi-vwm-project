class MutableTuple:
    # key..     car instance
    # value..   agregate func value
    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    # Return the key of the tuple
    def key(self):
        return self.__key

    # Return the value of the tuple
    def value(self):
        return self.__value

    # Comparision operator !!! Based on the value
    def __lt__(self, other):
        return self.value() < other.value()

    # String operator override
    def __str__(self):
        return "<" + str(self.key()) + ", " + str(self.value()) + ">"

    # The representation contains also an ID
    def __repr__(self):
        return str(id(self)) + "@" + self.__str__()
