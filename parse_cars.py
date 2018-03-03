import csv
from cars_data import Car

# http://nfs.wikia.com/wiki/Need_for_Speed:_Underground_2/Cars
# Path to the csv file
csv_path = "data/nsfmw2/cars_short.csv"
# The keys that are used to map the variables from the csv file
keys = ["name","acceleration","speed","handling"]

def parse_csv():
    # Array of dictionaries
    all_cars = [ ]
    with open(csv_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            try:
                # Zip the keys and values from the
                r = dict(zip(keys, row))
                # Convert the values to the integral types
                r['handling'] = int(r['handling'])
                r['acceleration'] = int(r['acceleration'])
                r['speed'] = int(r['speed'])
                all_cars.append(r)
            except csv.Error as e:
                print(e)
    return all_cars

def parse_csv_classes():
    # Array containing all instances of cars
    cars = [ ]
    # The individual arrays of KVP<car, parameter>
    cars_accel = {}
    cars_speed = {}
    cars_handl = {}
    with open(csv_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=';')
        for row in readCSV:
            try:
                # Zip the keys and values from the
                r = dict(zip(keys, row))
                # Convert the values to the intagral types
                name = r['name']
                r['handling'] = int(r['handling'])
                handling = r['handling']
                r['acceleration'] = int(r['acceleration'])
                acceleration = r['acceleration']
                r['speed'] = int(r['speed'])
                speed = r['speed']
                # Create a new instance of a car
                c = Car(name, acceleration, speed, handling)
                # Add the cars
                cars.append(c)
                cars_accel.update({c:acceleration})
                cars_handl.update({c:handling})
                cars_speed.update({c:speed})
            except csv.Error as e:
                print(e)

    return cars, sort_by_param(cars_accel), sort_by_param(cars_speed), sort_by_param(cars_handl)


def sort_by_param(d):
    return sorted(d.items(), key=lambda x: x[ 1 ])


if __name__ == "__main__":
    cars, cars_accel, cars_speed, cars_handl = parse_csv_classes()
    for i in cars_speed:
        print(i[0] + " " + str(i[1]))






