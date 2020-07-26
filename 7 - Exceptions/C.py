def test():
    try:
        colores = {'rojo': 'red', 'verde': 'green', 'negro': 'black'}
        colores['blanco']
    except KeyError:
        print("La key no existe")


test()
