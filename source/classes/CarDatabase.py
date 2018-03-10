import csv
import heapq as heap
from source.classes.Automobile import Automobile
from source.classes.MutableTuple import MutableTuple
from source.algorithms import agregate_sum_func
from source.classes.MyHeap import MyHeap

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
                    # Create a new empty car
                    car = Automobile()
                    # Create a tuple for each atribute
                    name_tuple = MutableTuple(car, row[0])
                    accel_tuple = MutableTuple(car, int(row[1]))
                    speed_tuple = MutableTuple(car, int(row[2]))
                    handl_tuple = MutableTuple(car, int(row[3]))
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

    def naive_rank_sort(self, checkbox_dict, agregate_func):
        # Create a new array with agregate values
        agregated = []
        for car in self.__cars:
            tuple = MutableTuple(car, agregate_func(car, checkbox_dict))
            agregated.append(tuple)
        agregated.sort(reverse=True)
        return agregated

    # 1. Compute overall score for every object by looking into each sorted list.
    # 2. Return k objects with the highest overall score.
    def naive_k(self, checkbox_dict, agregate_func, k):
        results = []
        for car in self.__cars:
            results.append(MutableTuple(car, agregate_func(car, checkbox_dict)))
        results.sort(reverse=True)
        return results[:k]

    # 1. Set the threshold t to be the aggregate of the scores seen in this access.
    # 2. Do random accesses and compute the scores of the seen objects.
    # 3. Maintain a list of top-k objects seen so far
    # 4. Stop, when the scores of the top-k are greater or equal to the threshold.
    # e. Return the top-k seen so far
    def top_k_treshold(self, checkbox_dict, agregate_func, k):
        my_heap = MyHeap(k)
        seen = set()

        for i in range(0, len(self.__cars)):
            # Get the row
            first_accel = self.__car_accel[i]
            first_speed = self.__car_speed[i]
            first_handl = self.__car_handl[i]
            # Set treshold
            treshold = first_accel.value() + first_speed.value() + first_handl.value()
            # Check if I found the target
            if not my_heap.set_treshold(treshold):
                break
            # Compute score of seen objects
            if not seen.__contains__(first_accel):
                seen.add(first_accel)
                fa = agregate_func(first_accel, checkbox_dict)
                my_heap.add_element(fa, first_accel)
            if not seen.__contains__(first_speed):
                seen.add(first_speed)
                fs = agregate_func(first_speed, checkbox_dict)
                my_heap.add_element(fs, first_speed)
            if not seen.__contains__(first_handl):
                seen.add(first_handl)
                fh = agregate_func(first_handl, checkbox_dict)
                my_heap.add_element(fh, first_handl)
