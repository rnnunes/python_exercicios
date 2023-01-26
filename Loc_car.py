import os



def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print('[{}] {} - R$ {} /dia'.format(i, car[0], car[1]))


def linha():
    print("==============================")



carros = [
    ("Chevrolet Tracker", 120),
    ("Chevrolet Onix", 90),
    ("Chevrolet Spin", 150),
    ("Hyundai Hb20", 85),
    ("Hyundai Tucson", 120),
    ("Fiat Uno", 60),
    ("Fiat Mobi", 70),
    ("Fiat Pulse", 130)
]
alugueis = []


while True:

        linha()
        print("Bem Vendo à locadora de carros!")
        linha()


        print("\nO que deseja fazer?")
        res = int(input('0 - Mostrar portifólio || 1 - Alugar um carro || 2 - Devolver um carro\n'))

        if res == 0:
                os.system('cls')
                mostrar_lista_de_carros(carros)

                print('')
                linha()
                res1 = int(input('0 - CONTINUAR | 1 - SAIR \n'))
                if res1 == 0:
                        os.system('cls')
                elif res1 == 1:
                       os.system('cls') 
                       break

        elif res == 1:
                os.system('cls')
                print('[- ALUGAR -] Dê uma olhada em nosso portifólio.\n')

                mostrar_lista_de_carros(carros)
                print('')

                linha()
                alugar = int(input('Escolha o código do carro: \n'))
                diaria = int(input('Insira a quantidade de dias que deseja alugar: \n'))
                os.system('cls')

                print('Você escolheu {} por {} dias.'.format(i([alugar], diaria)))
                print('O aluguel totalizaria R$ {}. Deseja algugar? \n\n'.format())

                linha()
                print('0 - SIM | 1 - NÃO')
                break