# Realiza un programa que pida al usuario cuantos números quiere introducir.
# Luego lee todos los números y realiza una media aritmética.

a = int(input("How many numbers would you like to add?: "))
total = 0

for n in range(a):
    total += int(input())

print(total / a)
