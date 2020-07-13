# Utilizando la función range() y la conversión a listas genera
# las siguientes listas dinámicamente:

# Todos los números del 0 al 10 [0, 1, 2, ..., 10]
# Todos los números del -10 al 0 [-10, -9, -8, ..., 0]
# Todos los números pares del 0 al 20 [0, 2, 4, ..., 20]
# Todos los números impares entre -20 y 0 [-19, -17, -15, ..., -1]
# Todos los números múltiples de 5 del 0 al 50 [0, 5, 10, ..., 50]

a = list(range(0, 11))
b = list(range(-10, 1))
c = list(range(0, 21, 2))
d = list(range(-19, 0, 2))
e = list(range(0, 51, 5))

print(a)
print(b)
print(c)
print(d)
print(e)