import csv


if __name__ == "__main__":
    with open("cars_mv_all.csv") as csv_file:
        read_csv = csv.reader(csv_file, delimiter='|')
        for row in read_csv:
            try:
                if len(row) == 7:
                    print(row[0] + ";" + str(int(row[4])) + ";" + str(int(row[5])) + ";" + str(int(row[6])))
                else:
                    print(row[0] + ";" + str(int(row[3])) + ";" + str(int(row[4])) + ";" + str(int(row[5])))
            except csv.Error as e:
                print(e)