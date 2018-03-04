class Automobile:
    acceleration = 0
    speed = 0
    handling = 0
    name = ""

    def __init__(self, __name, __acceleration, __speed, __handling):
        self.name = __name
        self.acceleration = __acceleration
        self.speed = __speed
        self.handling = __handling

    def __str__(self):
        return self.name + " - " + str(self.acceleration) + " " + str(self.speed) + " " + str(self.handling)
