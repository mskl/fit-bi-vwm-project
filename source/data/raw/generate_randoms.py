import csv
import random


def generate_random_values(csv_path="random_cars_names.csv"):
    with open(csv_path) as csv_file:
        read_csv = csv.reader(csv_file, delimiter=';')
        for row in read_csv:
            try:
                a = int(abs(random.gauss(0.3, 0.2)) * 100)
                h = int(abs(random.gauss(0.3, 0.2)) * 100)
                s = int(abs(random.gauss(0.3, 0.2)) * 100)

                print(row[0] + ";" + str(a) + ";" + str(s) + ";" + str(h))
            except csv.Error as e:
                print(e)


if __name__ == "__main__":
    generate_random_values()