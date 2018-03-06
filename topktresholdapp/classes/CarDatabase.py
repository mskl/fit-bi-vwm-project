import csv
from topktresholdapp.classes.Automobile import Automobile

# The keys that are used to map the variables from the csv file
keys = ["name","acceleration","speed","handling"]

class CarDatabase:
    # Array containing all instances of cars
    __cars = []
    # The individual arrays of KVP<car, parameter>
    __car_names = {}
    __car_accel = {}
    __car_speed = {}
    __car_handl = {}

    def __init__(self, csv_path):
        self.parse_csv_classes(csv_path)
        self.sort_all_arrays()

    def parse_csv_classes(self, csv_path):
        with open(csv_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                try:
                    # Zip the keys and values from the
                    r = dict(zip(keys, row))
                    # Convert the values to the integral types
                    name = r[ 'name' ]
                    r[ 'handling' ] = handling = int(r[ 'handling' ])
                    r[ 'acceleration' ] = acceleration = int(r[ 'acceleration' ])
                    r[ 'speed' ] = speed = int(r[ 'speed' ])
                    # Create a new instance of a car
                    c = Automobile(name, acceleration, speed, handling)
                    # Add the cars
                    self.__cars.append(c)
                    self.__car_names.update({c: name})
                    self.__car_accel.update({c: acceleration})
                    self.__car_handl.update({c: handling})
                    self.__car_speed.update({c: speed})
                except csv.Error as e:
                    print(e)

    @staticmethod
    def sort_by_param(d, reversed):
        def second_param(x):
            return x[1]
        return sorted(d.items(), key=second_param, reverse=reversed)

    def sort_all_arrays(self):
        self.__car_accel = self.sort_by_param(self.__car_accel, True)
        self.__car_speed = self.sort_by_param(self.__car_speed, True)
        self.__car_handl = self.sort_by_param(self.__car_handl, True)
        self.__car_names = self.sort_by_param(self.__car_names, False)

    def get_car_instances(self):
        return self.__cars

    def get_speed(self):
        return self.__car_speed

    def get_accel(self):
        return self.__car_accel

    def get_handl(self):
        return self.__car_handl

    def get_names(self):
        return self.__car_names

    @staticmethod
    def agregate_sum(car, a, s, h):
        sum = 0
        if a is True:
            sum += car.accel
        if s is True:
            sum += car.speed
        if h is True:
            sum += car.handl
        return sum

    @staticmethod
    def agregate_max(car, a, s, h):
        m = 0
        if a is True:
            m = max(m, car.accel)
        if s is True:
            m = max(m, car.speed)
        if h is True:
            m = max(m, car.handl)
        return m

    def naive_rank_sort(self, a, s, h, agregate_func):
        # Create a new array with agregate values
        agregate = {}
        for car in self.__cars:
            agregate.update({car:agregate_func(car, a, s, h)})
        return self.sort_by_param(agregate, True)