# Utilizando operadores lógicos, determina si una cadena
# de texto introducida por el usuario tiene una longitud
# mayor o igual que 3 y a su vez es menor que 10
# (es suficiene con mostrar True o False).

a = input("Texto: ")

print("El texto tiene mas de 3 (o 3) y menos de 10 caracteres",
      len(a) >= 3 and len(a) < 10)
