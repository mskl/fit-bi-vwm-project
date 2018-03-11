from flask import request
import time


# Process the GET parameters
def process_get_parameters():
    # The default values for the variables returned
    sort_checkbox = False, False, False
    sort_agregate = "sum"
    sort_algorithm = "naive"
    agregate_func = agregate_sum_func
    sort_quantity = 3

    # Obtain the GET parameters
    if request.method == "GET":
        # Values of checkboxes
        sort_checkbox = request.args.getlist('sort')
        # The sorting function
        sort_agregate = request.args.get('agregate')
        # The algorithm to get the top-k
        sort_algorithm = request.args.get('algorithm')
        # The treshold quantity
        sort_quantity = request.args.get('quantity', type=int)

    # Process the checkboxes
    checkbox_dict = {'accel': "accel" in sort_checkbox,
                     'speed': "speed" in sort_checkbox,
                     'handl': "handl" in sort_checkbox}

    # Process the agregate function from the get
    if sort_agregate == "sum":
        agregate_func = agregate_sum_func
    elif sort_agregate == "max":
        agregate_func = agregate_max_func

    return checkbox_dict, sort_agregate, sort_algorithm, agregate_func, sort_quantity


# Sum of all attributes specified in the checkbox dict
def agregate_sum_func(car, checkbox_dict):
    suma = 0
    if checkbox_dict['accel'] is True:
        suma += car.key().get_accel_value()
    if checkbox_dict['speed'] is True:
        suma += car.key().get_speed_value()
    if checkbox_dict['handl'] is True:
        suma += car.key().get_handl_value()
    return suma


# Max among all attributes in the checkbox dict
def agregate_max_func(car, checkbox_dict):
    maximum = 0
    if checkbox_dict['accel'] is True:
        maximum = max(maximum, car.key().get_accel_value())
    if checkbox_dict['speed'] is True:
        maximum = max(maximum, car.key().get_speed_value())
    if checkbox_dict['handl'] is True:
        maximum = max(maximum, car.key().get_handl_value())
    return maximum


# The wrapper that wraps any function and returns a (<return by func>, exec. time), tuple
def timed(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        q_time = time.time() - start
        return result, q_time
    return wrapper
