from flask import request
import time


# Process the GET parameters
def get_form_data():
    # Settings that are obtained from the GET
    sort_checkbox = request.args.getlist('sort')
    form_settings_dict = {'checkbox': {'accel': "accel" in sort_checkbox or False,
                                         'speed': "speed" in sort_checkbox or False,
                                         'handl': "handl" in sort_checkbox or False},
                          'agregate': request.args.get('agregate') or "sum",
                          'algorithm': request.args.get('algorithm') or "naive",
                          'quantity': request.args.get('quantity', type=int) or 3}
    # Return thr dict
    return form_settings_dict


# Sum of all attributes specified in the checkbox dict
def agregate_sum_func(car, form_data):
    soucet = 0
    if form_data['checkbox']['accel'] is True:
        soucet += car.key().get_accel_value()
    if form_data['checkbox']['speed'] is True:
        soucet += car.key().get_speed_value()
    if form_data['checkbox']['handl'] is True:
        soucet += car.key().get_handl_value()
    return soucet


# Max among all attributes in the checkbox dict
def agregate_max_func(car, form_data):
    maximum = 0
    if form_data['checkbox']['accel'] is True:
        maximum = max(maximum, car.key().get_accel_value())
    if form_data['checkbox']['speed'] is True:
        maximum = max(maximum, car.key().get_speed_value())
    if form_data['checkbox']['handl'] is True:
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
