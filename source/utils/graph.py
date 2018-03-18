import matplotlib.pyplot as plt
import numpy as np
import sys
import itertools
import random
from werkzeug.datastructures import *
from scipy.interpolate import spline


from source.classes.CarDatabase import CarDatabase
from source.algorithms import *

if __name__ == "__main__":
    car_database = CarDatabase("../../source/data/cars_random.csv")

    array_x = []
    array_y_naive = []
    array_y_topk = []

    for i in range(1, 7000):
        print(i)

        array_x.append(i)
        settings = MultiDict([('sort', 'accel'), ('sort', 'speed'), ('sort', 'handl'), ('quantity', i)])

        db_k, q_time_k = car_database.top_k_treshold(settings, agregate_sum_func)
        db_n, q_time_n = car_database.top_k_naive(settings, agregate_sum_func)

        array_y_naive.append(q_time_n)
        array_y_topk.append(q_time_k)

    poly_naive = np.polyfit(array_x, array_y_naive, 2)
    poly_naive_y = np.poly1d(poly_naive)(array_x)
    poly_topk = np.polyfit(array_x, array_y_topk, 2)
    poly_topk_y = np.poly1d(poly_topk)(array_x)

    plt.plot(array_x, poly_naive_y)
    plt.plot(array_x, poly_topk_y)

    #plt.plot(array_x, array_y_topk)
    #plt.plot(array_x, array_y_naive)
    plt.show()