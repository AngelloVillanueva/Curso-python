def divisors(num):
    divisors = []
    assert num > 0, "Debes ingresar un número positivo"
    for i in range(1,num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Ingresa un número: ")
    assert num.isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("Terminó el programa")
    

if __name__ == '__main__':
    run()