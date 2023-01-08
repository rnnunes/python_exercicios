from random import randint

while True:
    comando = int(input('Tente acertar o numero de 0 a 5!\n Insira o numero:'))

    x = randint(0,5)
    if comando == x:
        print('Parabens vc acertou o Numero {}.'.format(x))
        break
    else: 
        print('Errou, o numero era {}'.format(x))