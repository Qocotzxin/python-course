def test():
    try:
        return 15 + "20"
    except TypeError:
        print("No se puede sumar un string y un number")


test()