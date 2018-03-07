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

    def __eq__(self, another):
        return self.accel == another.accel and self.speed == another.speed and self.handl == another.handl and self.name == another.name

    def __hash__(self):
        return hash(self.name + str(self.accel)+ str(self.speed) + str(self.handl))

    def __str__(self):
        return self.name + " - " + str(self.accel) + " " + str(self.speed) + " " + str(self.handl)
