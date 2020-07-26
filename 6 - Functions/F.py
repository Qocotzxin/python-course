def separar(list):
    even = []
    odd = []
    for l in list:
        if l % 2 == 0:
            even.append(l)
        else:
            odd.append(l)
    return even, odd


pares, impares = separar([6, 5, 2, 1, 7])
print(pares)
print(impares)
