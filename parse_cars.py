import csv
import sys

# http://nfs.wikia.com/wiki/Need_for_Speed:_Underground_2/Cars
csv_path = "data/nsfmw2/cars_nsfmw2.csv"

def parse_csv():
    all_cars = [ ]
    with open(csv_path) as csvfile:
        readCSV = csv.reader(csvfile, delimiter='|')
        for row in readCSV:
            try:
                all_cars.append(row)
            except csv.Error as e:
                print(e)

    # Transform into a dictionary
    keys = ["image","name","manufacturer","model","unlock","acceleration","speed","handling","hundred","topspeed","torque","power"]
    return dict(zip(keys, zip(*all_cars)))

if __name__ == "__main__":
    print(parse_csv())

