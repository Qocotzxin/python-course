# Realiza un programa que lea dos números por teclado y permita elegir
# entre 3 opciones en un menú:

# Mostrar una suma de los dos números
# Mostrar una resta de los dos números (el primero menos el segundo)
# Mostrar una multiplicación de los dos números
# En caso de introducir una opción inválida, el programa informará de que no es correcta.

a = int(input("First number: "))
b = int(input("Second number: "))
option = int(
    input("""
    Opciones:
    1) - Sum
    2) - Rest
    3) - Multiply
 """))

if option == 1:
    print(a + b)
elif option == 2:
    print(a - b)
elif option == 3:
    print(a * b)
else:
    print("Not a valid option")