from flask import request
import time


# Sum of all attributes specified in the checkbox dict
def aggregate_sum_func(car, _a, _s, _h):
    soucet = 0
    if _a:
        soucet += car.key().get_accel_value()
    if _s:
        soucet += car.key().get_speed_value()
    if _h:
        soucet += car.key().get_handl_value()
    return soucet


# Max among all attributes in the checkbox dict
def aggregate_max_func(car, _a, _s, _h):
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
        return result, q_time   # Q-time will be the last element
    return wrapper


# Get the aggregate function from the form values data (GET or POST)
def get_aggregate_function(form_data):
    # Process the aggregate function from the get
    if form_data.get('agregate') == "max":
        return aggregate_max_func
    else:
        return aggregate_sum_func


# Check if the key was seen in all sets
def seen_in_all_func(key, set_a, set_s, set_h, a, s, h):
    if a and (key not in set_a):
        return False
    elif s and (key not in set_s):
        return False
    elif h and (key not in set_h):
        return False
    else:
        return True


# Parse the MultiDict from the form and return a s h
def get_ash_from_form_values(form_values):
    a = 'accel' in form_values.getlist('sort')
    s = 'speed' in form_values.getlist('sort')
    h = 'handl' in form_values.getlist('sort')
    return a, s, h


# Parse the MultiDict from the form and return the quantity
def get_quantity_from_form_values(form_values):
    return form_values.get('quantity', default=15, type=int)