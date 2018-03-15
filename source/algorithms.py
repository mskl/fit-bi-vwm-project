from flask import request
import time


# Sum of all attributes specified in the checkbox dict
def agregate_sum_func(car, _a, _s, _h):
    soucet = 0
    if _a:
        soucet += car.key().get_accel_value()
    if _s:
        soucet += car.key().get_speed_value()
    if _h:
        soucet += car.key().get_handl_value()
    return soucet


# Max among all attributes in the checkbox dict
def agregate_max_func(car, _a, _s, _h):
    maximum = 0
    if _a:
        maximum = max(maximum, car.key().get_accel_value())
    if _s:
        maximum = max(maximum, car.key().get_speed_value())
    if _h:
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
        return agregate_max_func
    else:
        return agregate_sum_func
