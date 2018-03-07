
# Extracts Accel, Speed, Handling from list and return bool tuple
def ash_from_post_list(lst):
    a = "accel" in lst
    s = "speed" in lst
    h = "handl" in lst
    return a, s, h