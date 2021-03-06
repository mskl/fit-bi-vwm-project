import matplotlib.pyplot as plt
import numpy as np
from werkzeug.datastructures import *

from source.classes.CarDatabase import CarDatabase
from source.utils.algorithms import *

if __name__ == "__main__":
    car_database = CarDatabase("data/cars_random.csv")

    array_x = []
    array_y_naive = []
    array_y_topk = []
    array_y_fagin = []

    for i in range(1, 7000, 50):
        print(i)
        settings = MultiDict([('sort', 'accel'), ('sort', 'speed'), ('sort', 'handl'), ('quantity', i)])

        array_x.append(i)
        (db_k, acces_count_k),q_time_k = car_database.top_k_treshold(settings, aggregate_sum_func)
        (db_n, acces_count_n),q_time_n = car_database.top_k_naive(settings, aggregate_sum_func)
        (db_f, acces_count_f),q_time_f = car_database.top_k_fagin(settings, aggregate_sum_func)
        array_y_naive.append(acces_count_n)
        array_y_topk.append(acces_count_k)
        array_y_fagin.append(acces_count_f)

    poly_naive = np.polyfit(array_x, array_y_naive, 1)
    poly_naive_y = np.poly1d(poly_naive)(array_x)
    poly_topk = np.polyfit(array_x, array_y_topk, 3)
    poly_topk_y = np.poly1d(poly_topk)(array_x)
    poly_fagin = np.polyfit(array_x, array_y_fagin, 3)
    poly_fagin_y = np.poly1d(poly_fagin)(array_x)

    fig, ax = plt.subplots()
    ax.plot(array_x, poly_naive_y, label="naive")
    ax.plot(array_x, poly_topk_y, label="top-k")
    ax.plot(array_x, poly_fagin_y, label="fagin")
    fig.tight_layout()
    # Now add the legend with some customizations.
    legend = ax.legend(loc='upper center', shadow=True)

    plt.show()