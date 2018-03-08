# Extracts Accel, Speed, Handling from list and return bool tuple
def ash_from_post_list(lst):
    a = "accel" in lst
    s = "speed" in lst
    h = "handl" in lst
    return a, s, h


def agregate_sum_func(car, a, s, h):
    sum = 0
    if a is True:
        sum += car.get_accel_value()
    if s is True:
        sum += car.get_speed_value()
    if h is True:
        sum += car.get_handl_value()
    return sum


def agregate_max_func(car, a, s, h):
    m = 0
    if a is True:
        m = max(m, car.get_accel_value())
    if s is True:
        m = max(m, car.get_speed_value())
    if h is True:
        m = max(m, car.get_handl_value())
    return m