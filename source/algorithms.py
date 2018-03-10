# Extracts Accel, Speed, Handling from list and return bool tuple
def ash_from_post_list(lst):
    a = "accel" in lst
    s = "speed" in lst
    h = "handl" in lst
    return a, s, h


# Sum of all attributes specified in the checkbox dict
def agregate_sum_func(car, checkbox_dict):
    sum = 0
    if checkbox_dict['accel'] is True:
        sum += car.get_accel_value()
    if checkbox_dict['speed'] is True:
        sum += car.get_speed_value()
    if checkbox_dict['handl'] is True:
        sum += car.get_handl_value()
    return sum


# Max among all attributes in the checkbox dict
def agregate_max_func(car, checkbox_dict):
    m = 0
    if checkbox_dict[ 'accel' ] is True:
        m = max(m, car.get_accel_value())
    if checkbox_dict[ 'speed' ] is True:
        m = max(m, car.get_speed_value())
    if checkbox_dict[ 'handl' ] is True:
        m = max(m, car.get_handl_value())
    return m
