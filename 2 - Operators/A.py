# Realiza un programa que lea 2 números por teclado y determine los
# siguientes aspectos (es suficiene con mostrar True o False):

# Si los dos números son iguales
# Si los dos números son diferentes
# Si el primero es mayor que el segundo
# Si el segundo es mayor o igual que el primero

a = float(input('First number: '))
b = float(input('Second number: '))

print("Son iguales?: ", a == b)
print("Son distintos?: ", a != b)
print("El primero es mayor?: ", a > b)
print("El segundo es mayor o igual que el primero?: ", a <= b)
