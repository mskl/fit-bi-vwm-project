class Automobile:
    def __init__(self):
        self.name = None
        self.accel = None
        self.speed = None
        self.handl = None

    # Contains references to the MutableTuple objects
    def assign(self, _name, _accel, _speed, _handl):
        self.name = _name
        self.accel = _accel
        self.speed = _speed
        self.handl = _handl

    def get_name_value(self):
        return self.name.value()

    def get_accel_value(self):
        return self.accel.value()

    def get_speed_value(self):
        return self.speed.value()

    def get_handl_value(self):
        return self.handl.value()

    # A hack to make itself compatible with the MutableTuple
    def key(self):
        return self

    def __str__(self):
        return str(self.get_name_value()) \
               + " - " + str(self.get_accel_value()) \
               + " " + str(self.get_speed_value()) \
               + " " + str(self.get_handl_value())
