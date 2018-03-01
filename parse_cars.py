import csv
import sys

# http://nfs.wikia.com/wiki/Need_for_Speed:_Underground_2/Cars
csv_path = "data/nsfmw2/cars_nsfmw2.csv"
keys = ["image","name","manufacturer","model","unlock","acceleration",
        "speed","handling","hundred","topspeed","torque","power"]

def index_from_key(key):
    for k in range(0, len(keys)):
        if key == keys[k]:
            return k
    return None

def parse_csv():
    # Array of dictionaries
    all_cars = [ ]
    with open(csv_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            r = dict(zip(keys, row))
            try:
                all_cars.append(r)
            except csv.Error as e:
                print(e)
    return all_cars

if __name__ == "__main__":
    parsed = parse_csv()
    parsed[ 0 ][ "name" ]
