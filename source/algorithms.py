from flask import request
import time

# Sum of all attributes specified in the checkbox dict
def agregate_sum_func(car, form_data):
    soucet = 0
    checkbox_list = form_data.getlist('sort')
    print(checkbox_list)
    if 'accel' in checkbox_list:
        soucet += car.key().get_accel_value()
    if 'speed' in checkbox_list:
        soucet += car.key().get_speed_value()
    if 'handl' in checkbox_list:
        soucet += car.key().get_handl_value()
    return soucet


# Max among all attributes in the checkbox dict
def agregate_max_func(car, form_data):
    maximum = 0
    checkbox_list = form_data.getlist('sort')
    if 'accel' in checkbox_list:
        maximum = max(maximum, car.key().get_accel_value())
    if 'speed' in checkbox_list:
        maximum = max(maximum, car.key().get_speed_value())
    if 'handl' in checkbox_list:
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


# Get the agregate function from the form values data (GET or POST)
def get_agregate_function(form_data):
    # Process the agregate function from the get
    if form_data.get('agregate') == "max":
        return agregate_sum_func
    else:
        return agregate_max_func
