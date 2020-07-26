def test():
    try:
        lista = [1, 2, 3, 4, 5]
        return lista[10]
    except IndexError:
        print("El indice no existe")


test()