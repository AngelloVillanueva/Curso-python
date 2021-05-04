def es_capicua(a):
    
    if a == a[::-1]:
        print('Es cap')
        return True
    elif a != a[::-1]:
        a = str(int(a)*2)
        print(a)
        es_capicua(a)
   #b = a[::-1]

if __name__=='__main__':
    a = input('Engresa un numero: ')
    es_capicua(a)

    