def es_primo(a):
    numbers = [i for i in range(1,a+1) if a % (i) == 0]
    print(numbers)
    if len(numbers) == 2:
        print("Es primo")
        return True


def es_antiprimo(a):
    numbers = [i for i in range(1,a+1) if a % (i) == 0]
    if len(numbers) != 2:
        return True


def divisores_comun(a,b):
    numbers_a = [i for i in range(1,a+1) if a % (i) == 0]
    numbers_b = [i for i in range(1,b+1) if b % (i) == 0]
    lista = []

    for i in numbers_a:
        if i in numbers_b:
            lista.append(i)
    for i in lista:
        print(i)



if __name__ == '__main__':
    a = int(input(''))
    b = int(input(''))
    es_primo(a)
    es_antiprimo(a)
    divisores_comun(a, b)