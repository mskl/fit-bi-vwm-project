import csv
from Automobile import Automobile

# The keys that are used to map the variables from the csv file
keys = ["name","acceleration","speed","handling"]

class CarDatabase:
    # Array containing all instances of cars
    __cars = []
    # The individual arrays of KVP<car, parameter>
    __car_accel = {}
    __car_speed = {}
    __car_handl = {}

    # The tuple containing all info
    # all_cars = []

    def __init__(self, csv_path):
        self.parse_csv_classes(csv_path)
        self.sort_all()

    def parse_csv_classes(self, csv_path):
        with open(csv_path) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=';')
            for row in readCSV:
                try:
                    # Zip the keys and values from the
                    r = dict(zip(keys, row))
                    # Convert the values to the integral types
                    name = r[ 'name' ]
                    r[ 'handling' ] = int(r[ 'handling' ])
                    handling = r[ 'handling' ]
                    r[ 'acceleration' ] = int(r[ 'acceleration' ])
                    acceleration = r[ 'acceleration' ]
                    r[ 'speed' ] = int(r[ 'speed' ])
                    speed = r[ 'speed' ]
                    # Create a new instance of a car
                    c = Automobile(name, acceleration, speed, handling)
                    # Add the cars
                    self.__cars.append(c)
                    # self.all_cars.append(r)
                    self.__car_accel.update({c: acceleration})
                    self.__car_handl.update({c: handling})
                    self.__car_speed.update({c: speed})
                except csv.Error as e:
                    print(e)

    @staticmethod
    def sort_by_param(d, reversed):
        return sorted(d.items(), key=lambda x: x[ 1 ], reverse=reversed)

    def sort_all(self):
        self.__car_accel = self.sort_by_param(self.__car_accel, True)
        self.__car_speed = self.sort_by_param(self.__car_speed, True)
        self.__car_handl = self.sort_by_param(self.__car_handl, True)

    def get_car_instances(self):
        return self.__cars

    def get_speed(self):
        return self.__car_speed

    def get_accel(self):
        return self.__car_accel

    def get_handl(self):
        return self.__car_handl