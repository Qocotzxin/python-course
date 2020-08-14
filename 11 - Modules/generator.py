import random
import math


def read_number(init, final, message):
    while True:
        try:
            value = int(input(message))
        except:
            print("Error: not a valid number, please try again")
        else:
            if value >= init and value <= final:
                return value


def generator():
    numbers = read_number(
        1, 20, "¿Cuantos números quieres generar? [1 - 20]: ")
    mode = read_number(
        1, 3, "¿Cómo quieres redondear los números? [1] - Al alza, [2] - A la baja, [3] - Normal: ")
    random_list = []

    if mode == 1:
        round_function = math.ceil
    if mode == 2:
        round_function = math.floor
    if mode == 3:
        round_function = round

    for n in range(numbers):
        random_number = random.uniform(0, 101)
        print("Random number: "  + str(random_number))
        rounded_random = round_function(random_number)
        print("Rounded random number: "  + str(rounded_random))
        random_list.append(rounded_random)

    return random_list


generator()
