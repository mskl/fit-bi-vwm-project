import csv
from source.utils.algorithms import *
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
        # Create a new car for a reference
        car = Automobile()
        # Create a tuple for each attribute
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

    @staticmethod
    def __get_treshold(a, s, h, aval, sval, hval):
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

        # Count the number of random accesses
        access_count = 0

        results = []
        a, s, h = get_ash_from_form_values(form_values)
        quantity = get_quantity_from_form_values(form_values)
        for car in self.__cars:
            access_count += 1
            agregated = agregate_func(car, a, s, h)
            results.append(MutableTuple(car, agregated))
        results.sort(reverse=True)
        if quantity != 0:
            return (results[:quantity], access_count)
        else:
            return (results, access_count)

    @timed
    def top_k_fagin(self, form_values, aggregate_func):
        # 1. Sequentially access all the sorted lists in parallel until there are k objects
        #       that have been seen in all lists.
        # 2. Perform random accesses to obtain the scores of all seen objects
        # 3. Compute score for all objects and return the top-k

        # Keep the sets of objects
        seen_a = set()
        seen_s = set()
        seen_h = set()
        seen_in_all = set()

        # Count the number of random accesses
        access_count = 0

        # Parse the values from the form
        quantity = get_quantity_from_form_values(form_values)
        a, s, h = get_ash_from_form_values(form_values)

        # Iterate all sorted lists in parallel
        for i in range(0, len(self.__cars)):
            access_count += 1
            if a:
                seen_a.add(self.__car_accel[i].key())
                if seen_in_all_func(self.__car_accel[i].key(), seen_a, seen_s, seen_h, a, s, h):
                    seen_in_all.add(self.__car_accel[i].key())
            if s:
                seen_s.add(self.__car_speed[i].key())
                if seen_in_all_func(self.__car_speed[i].key(), seen_a, seen_s, seen_h, a, s, h):
                    seen_in_all.add(self.__car_speed[i].key())
            if h:
                seen_h.add(self.__car_handl[i].key())
                if seen_in_all_func(self.__car_handl[i].key(), seen_a, seen_s, seen_h, a, s, h):
                    seen_in_all.add(self.__car_handl[i].key())

            # If seen enough objects break and compute the scores
            if len(seen_in_all) >= quantity:
                break

        # Compute the results
        results = []
        for car in seen_in_all:
            aggregated = aggregate_func(car, a, s, h)
            results.append(MutableTuple(car, aggregated))

        # Sort the results and return
        results.sort(reverse=True)
        return results[:quantity], access_count

    @timed
    def top_k_treshold(self, form_values, agregate_func, srtd=True):
        # 1. Set the threshold t to be the aggregate of the scores seen in this access.
        # 2. Do random accesses and compute the scores of the seen objects.
        # 3. Maintain a list of top-k objects seen so far
        # 4. Stop, when the scores of the top-k are greater or equal to the threshold.
        # end. Return the top-k seen so far

        # Heap contains <agregate_value, car>
        my_heap = MyHeap(get_quantity_from_form_values(form_values))

        # Count the number of random accesses
        access_count = 0

        # Set of the objects that i've explored
        seen = set()
        a, s, h = get_ash_from_form_values(form_values)

        for i in range(0, len(self.__cars)):
            access_count += 1

            # Get the cars from the current row
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
                my_heap.add_element(first_accel, agregate_func(first_accel, a, s, h))
            if first_speed.key() not in seen:
                seen.add(first_speed.key())
                my_heap.add_element(first_speed, agregate_func(first_speed, a, s, h))
            if first_handl.key() not in seen:
                seen.add(first_handl.key())
                my_heap.add_element(first_handl, agregate_func(first_handl, a, s, h))

        if srtd:
            return my_heap.get_sorted_elements(), access_count
        else:
            return my_heap.get_unsorted_heap(), access_count

