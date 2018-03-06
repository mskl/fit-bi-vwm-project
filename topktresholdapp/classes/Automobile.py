class Automobile:
    accel = 0
    speed = 0
    handl = 0
    name = ""

    def __init__(self, _name, _accel, _speed, _handl):
        self.name = _name
        self.accel = _accel
        self.speed = _speed
        self.handl = _handl

    @property
    def __str__(self):
        return self.name + " - " + str(self.accel) + " " + str(self.speed) + " " + str(self.handl)
