import csv
from source.algorithms import *
from source.classes.Automobile import Automobile
from source.classes.MutableTuple import MutableTuple
from source.classes.MyHeap import MyHeap


''' The DB structure of the CarDatabase. 
                                         
   __car_names       __car_accel       __car_speed       __car_handl   
┌───────┬───────┐ ┌───────┬───────┐ ┌───────┬───────┐ ┌───────┬───────┐
│  car  │ name  │ │  car  │ accel │ │  car  │ speed │ │  car  │ handl │
└───────┴───────┘ └───────┴───────┘ └───────┴───────┘ └───────┴───────┘
    ▲                 ▲                 ▲                 ▲            
    ├─────────────────┴─────────────────┴─────────────────┘            
    ▼  __car_names,.. = [MutableTuple<car_instance, value>]                    
┌───────┐                                                              
│  car  │ __cars  = [car instance]                                                
└───────┘                                                                                                 
'''


class CarDatabase:
    # Array containing all instances of cars
    __cars = []
    # The individual arrays of KVP<car, parameter>
    __car_names = []
    __car_accel = []
    __car_speed = []
    __car_handl = []

    def __init__(self, csv_path):
        self.set_database(csv_path)

    def set_database(self, csv_path):
        del self.__cars[:]
        del self.__car_names[:]
        del self.__car_accel[:]
        del self.__car_speed[:]
        del self.__car_handl[:]

        # Parse the CSV document and save the values to my lists
        self.__parse_csv_classes(csv_path)
        # Sort all subarrays
        self.__sort_all_arrays()

    def __add_car(self, name, accel, speed, handl):
        car = Automobile()
        # Create a tuple for each atribute
        name_tuple = MutableTuple(car, name)
        accel_tuple = MutableTuple(car, speed)
        speed_tuple = MutableTuple(car, accel)
        handl_tuple = MutableTuple(car, handl)
        # Assign the tuples to the car
        car.assign(name_tuple, accel_tuple, speed_tuple, handl_tuple)
        # Add the individual lists
        self.__cars.append(car)
        self.__car_names.append(name_tuple)
        self.__car_accel.append(accel_tuple)
        self.__car_speed.append(speed_tuple)
        self.__car_handl.append(handl_tuple)

    def __parse_csv_classes(self, csv_path):
        with open(csv_path) as csv_file:
            read_csv = csv.reader(csv_file, delimiter=';')
            for row in read_csv:
                try:
                    self.__add_car(row[0], int(row[1]), int(row[2]), int(row[3]))
                except csv.Error as e:
                    print(e)

    def __sort_all_arrays(self):
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

    def __get_treshold(self, a, s, h, aval, sval, hval):
        treshold = 0
        if a:
            treshold += aval
        if s:
            treshold += sval
        if h:
            treshold += hval
        return treshold

    @timed
    def top_k_naive(self, form_values, agregate_func):
        # 1. Compute overall score for every object by looking into each sorted list.
        # 2. Return k objects with the highest overall score.
        results = []
        a = 'accel' in form_values.getlist('sort')
        s = 'speed' in form_values.getlist('sort')
        h = 'handl' in form_values.getlist('sort')
        for car in self.__cars:
            agregated = agregate_func(car, a, s, h)
            results.append(MutableTuple(car, agregated))
        results.sort(reverse=True)
        return results[:form_values.get('quantity', type=int, default=10)]

    @timed
    def top_k_treshold(self, form_values, agregate_func):
        # 1. Set the threshold t to be the aggregate of the scores seen in this access.
        # 2. Do random accesses and compute the scores of the seen objects.
        # 3. Maintain a list of top-k objects seen so far
        # 4. Stop, when the scores of the top-k are greater or equal to the threshold.
        # end. Return the top-k seen so far

        # Heap contains <agregate_value, car>
        my_heap = MyHeap(form_values.get('quantity', default=10, type=int))

        # Set of the objects that i've explored
        seen = set()
        a = 'accel' in form_values.getlist('sort')
        s = 'speed' in form_values.getlist('sort')
        h = 'handl' in form_values.getlist('sort')

        for i in range(0, len(self.__cars)):
            first_accel = self.__car_accel[i]
            first_speed = self.__car_speed[i]
            first_handl = self.__car_handl[i]

            # Compute the treshold for a row
            treshold = self.__get_treshold(a, s, h, first_accel.value(), first_speed.value(), first_handl.value())

            # If I found the target the alg should end (set_treshold returned true => END)
            if my_heap.set_treshold(treshold):
                break

            # Compute score of seen objects
            if first_accel.key() not in seen:
                seen.add(first_accel.key())
                fa = agregate_func(first_accel, a, s, h)
                my_heap.add_element(first_accel, fa)
            if first_speed.key() not in seen:
                seen.add(first_speed.key())
                fs = agregate_func(first_speed, a, s, h)
                my_heap.add_element(first_speed, fs)
            if first_handl.key() not in seen:
                seen.add(first_handl.key())
                fh = agregate_func(first_handl, a, s, h)
                my_heap.add_element(first_handl, fh)

        return my_heap.get_sorted_elements()

