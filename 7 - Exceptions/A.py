def division():
    try:
        return 10 / 0
    except ZeroDivisionError:
        print("No se puede dividir por cero.")


division()