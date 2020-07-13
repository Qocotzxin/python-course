# Realiza un programa que lea un número impar por teclado.
# Si el usuario no introduce un número impar, debe repetise
# el proceso hasta que lo introduzca correctamente.

while True:
    a = int(input("Type an odd number: "))

    if a % 2 != 0:
        print("Correcto")
        break
