def dec(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result, 3
    return wrapper

@dec
def foo():
    return {'a':1, 'b':2}

if __name__ == "__main__":
    result = foo()
    print(result)