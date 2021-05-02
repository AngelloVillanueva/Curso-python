# Este programa de black jack fue escrito para utilizarse en un desafio
# hecho por HackerRank.com, por lo que solo funciona bajo las condiciones 
# que Hacker Rank necesitaba.

def run():
    a = []
    while True:
        cj = (input(''))
        if cj != "STOP":
            a.append(int(cj))
        else:
            break
    suma_cj = sum(a)


    b = []
    cant_cartas = int(input(''))
    for i in range(cant_cartas):
        entrada = int(input(''))
        b.append(entrada)
    suma_cm = sum(b)
    
    if suma_cj == 21:
        print('Gana el jugador')
    elif suma_cj < 21:
        if suma_cj > suma_cm:
            print('Gana el jugador')
        elif suma_cm > 21:
            print('Gana el jugador')
        else:
            print('Gana la mesa')
    elif suma_cj > 21:
        print('Gana la mesa')

if __name__=='__main__':
    run()