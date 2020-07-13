# La siguiente matriz (o lista con listas anidadas) debe cumplir una condición,
# y es que en cada fila el cuarto elemento siempre debe ser el resultado de sumar
# los tres primeros. ¿Eres capaz de modificar las sumas incorrectas utilizando la
# técnica del slicing?

matriz = [[1, 1, 1, 3], [2, 2, 2, 7], [3, 3, 3, 9], [4, 4, 4, 13]]

for m in matriz:
    m[-1] = sum(m[:3])

print(matriz)
