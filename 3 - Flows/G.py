# Dadas dos listas, debes generar una tercera con todos los elementos
# que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:

lista_1 = ["h", 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
lista_2 = ["h", 'o', 'l', 'a', ' ', 'l', 'u', 'n', 'a']

lista_3 = []

for char in lista_1:
    if char in lista_2 and char not in lista_3:
        lista_3.append(char)

print(lista_3)