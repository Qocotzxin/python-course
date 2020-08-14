# Crea una función modificar() que a partir de una lista de números realice las siguientes tareas 
# sin modificar la original:

# Borrar los elementos duplicados.
# Ordenar la lista de mayor a menor.
# Eliminar todos los números impares.
# Realizar una suma de todos los números que quedan.
# Añadir como primer elemento de la lista la suma realizada.
# Devolver la lista modificada.
# Finalmente, después de ejecutar la función, comprueba que la suma de todos los números a partir del segundo, 
# concuerda con el primer número de la lista, tal que así:

import copy

numbers = [29, -5, -12, 17, 5, 24, 5, 12, 23, 16, 12, 5, -12, 17]

def modify(numbers):
    list_copy = list(set(numbers))
    list_copy.sort(reverse=True)
    even = list(filter(lambda x: x % 2 == 0, list_copy))
    even.insert(0, sum(even))
    return even

new_list = modify(numbers)
print(new_list)
print( new_list[0] == sum(new_list[1:]) )
