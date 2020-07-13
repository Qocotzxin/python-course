# Realiza un programa que pida al usuario un número entero del 0 al 9,
# y que mientras el número no sea correcto se repita el proceso.
# Luego debe comprobar si el número se encuentra en la
# lista de números y notificarlo:

numbers = [1, 3, 6, 9]
a = -1

while a < 0 or a > 9:
    a = int(input("Enter a number between 0 and 9: "))
    if a in numbers:
        print("The number is in the list")
