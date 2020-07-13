#Al realizar una consulta en un registro hemos obtenido una cadena de texto corrupta
# al revés. Al parecer contiene el nombre de un alumno y la nota de un exámen.
#¿Cómo podríamos formatear la cadena y conseguir una estructura como la siguiente?
# Nombre Apellido ha sacado un Nota de nota.

cadena = "zeréP nauJ,01"

result = cadena[::-1]

print(result)