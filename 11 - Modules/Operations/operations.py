
def error_type(list, division=False):
    error = None

    if division == True and list[-1] == 0:
        error = ZeroDivisionError("No es posible dividir entre cero.")

    for n in list:
        if type(n).__name__ != "int":
            error = TypeError("Tipo de dato no válido.")

    return error


def op_sum(first, second):
    error = error_type([first, second])
    if error == None:
        return first + second
    else:
        raise error

def op_subtract(first, second):
    error = error_type([first, second])
    if error == None:
        return first - second
    else:
        raise error

def op_multiply(first, second):
    error = error_type([first, second])
    if error == None:
        return first * second
    else:
        raise error

def op_divide(first, second):
    error = error_type([first, second], True)
    if error == None:
        return first / second
    else:
        raise error
