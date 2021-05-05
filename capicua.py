# def es_capicua(a):
#     if a == a[::-1]:
#         return True


# def calcular_capicua(a):
#     if a != a[::-1]:
#         b = int(a) + int(a[::-1])
#         calcular_capicua(str(b))
#     elif a == a[::-1]:
#         print(a)


def encontrar_capicua(a):
    if a != a[::-1]:
        b = abs(int(a[::-1]) - int(a)))
        print(b)
        encontrar_capicua(str(b))
        


if __name__=='__main__':
    a = input('Engresa un numero: ')
    es_capicua(a)
    # calcular_capicua(a)
    # encontrar_capicua(a)