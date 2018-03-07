import csv
from source.classes.Automobile import Automobile
from source.classes.MutableTuple import MutableTuple

# The keys that are used to map the variables from the csv file
keys = ["name","acceleration","speed","handling"]

class CarDatabase:
    # Array containing all instances of cars
    __cars = []
    # The individual arrays of KVP<car, parameter>
    __car_names = []
    __car_accel = []
    __car_speed = []
    __car_handl = []

    def __init__(self, csv_path):
        # Parse the CSV document and save the values to my lists
        self.parse_csv_classes(csv_path)
        # Sort all subarrays
        self.sort_all_arrays()

    def parse_csv_classes(self, csv_path):
        with open(csv_path) as csv_file:
            read_csv = csv.reader(csv_file, delimiter=';')
            for row in read_csv:
                try:
                    # Zip the keys and values from the CSV reader
                    r = dict(zip(keys, row))
                    # Convert the values to the integral types
                    name = r['name']
                    handl = int(r['handling'])
                    accel = int(r['acceleration'])
                    speed = int(r['speed'])
                    # Create a new empty car
                    car = Automobile()
                    # Create a tuple for each atribute
                    name_tuple = MutableTuple(car, name)
                    accel_tuple = MutableTuple(car, accel)
                    speed_tuple = MutableTuple(car, speed)
                    handl_tuple = MutableTuple(car, handl)
                    # Assign the tuples to the car
                    car.assign(name_tuple, accel_tuple, speed_tuple, handl_tuple)
                    # Add the individual lists
                    self.__cars.append(car)
                    self.__car_names.append(name_tuple)
                    self.__car_accel.append(accel_tuple)
                    self.__car_speed.append(speed_tuple)
                    self.__car_handl.append(handl_tuple)
                except csv.Error as e:
                    print(e)

    def sort_all_arrays(self):
        self.__car_accel.sort(reverse=True)
        self.__car_speed.sort(reverse=True)
        self.__car_handl.sort(reverse=True)
        self.__car_names.sort(reverse=False)

    def get_cars(self):
        return self.__cars

    def get_names(self):
        return self.__car_names

    def get_accel(self):
        return self.__car_accel

    def get_speed(self):
        return self.__car_speed

    def get_handl(self):
        return self.__car_handl

    def naive_rank_sort(self, a, s, h, agregate_func):
        # Create a new array with agregate values
        agregated = []
        for car in self.__cars:
            tuple = MutableTuple(car, agregate_func(car, a, s, h))
            agregated.append(tuple)
        agregated.sort(reverse=True)
        return agregated
#
    #def topk_agregate_sum(self, car, a, s, h):
    #    sum = 0
    #    if a is True:
    #        sum += self.__car_accel[ car ][ 0 ]
    #    if s is True:
    #        sum += self.__car_speed[ car ][ 0 ]
    #    if h is True:
    #        sum += self.__car_handl[ car ][ 0 ]
    #    return sum
#
    ## 1. Compute overall score for every object by looking into each sorted list.
    ## 2. Return k objects with the highest overall score.
    #def naive_k(self, a, s, h, agregate_func, k):
    #    results_work = {}
    #    for c in self.__cars:
    #        res = self.topk_agregate_sum(c, a, s, h)
    #        results_work.update({c: res})
    #    return results_work

if __name__ == "__main__":
    car_db = CarDatabase2("../data/nsfmw2/cars_short.csv")