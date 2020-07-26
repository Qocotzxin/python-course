# Crea un script llamado descomposicion.py que realice las siguientes tareas:

# Debe tomar 1 argumento que será un número entero positivo.
# En caso de no recibir un argumento, debe mostrar información acerca de cómo utilizar el script.
# El objetivo del script es descomponer el número en unidades, decenas, centenas, miles...
# tal que por ejemplo si se introduce el número 3647, el programa deberá devolver
# una descomposición línea a línea como la siguiente utilizando las técnicas de formateo:

# 0007
# 0040
# 0600
# 3000

import sys

if len(sys.argv) == 2 and int(sys.argv[1]) > 0:
    num = str(sys.argv[1])[::-1]
    base = "1".ljust(len(num) - 1, "0")
    unit = 1
    for n in range(len(num)):
        number = str(int(num[n]) * unit)
        print(number.rjust(len(base) + len(number), "0"))
        unit = unit * 10
        base = base[:-1]

else:
    print("Please enter a positive integer as argument")