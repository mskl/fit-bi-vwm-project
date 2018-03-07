from source.classes.Automobile import Automobile

if __name__ == "__main__":

    a = Automobile("ford", 0, 1, 2)
    b = Automobile("mazda", 3, 4, 5)

    d = {}

    d.update({a: 123})
    d.update({b: 456})

    print(d)
    print(d[a])
