def agregar_una_vez(lista, el):
    try:
        if el in lista:
            raise ValueError

        else:
            lista.append(el)
    except ValueError:
        print("Error: Imposible añadir elementos duplicados => [elemento].")


agregar_una_vez([1, 2, 3, 4], 4)
