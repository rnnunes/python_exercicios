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
        res = int(input('0 - Mostrar portifólio | 1 - Alugar um carro | 2 - Devolver um carro | 3 - Sair\n'))

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

                if len(carros) == 0:
                        print('Infelizmente todos os carros já foram alugados, por favor aguarde!')

                        linha()
                        res7 = int(input('0 - CONTINUAR | 1 - SAIR\n'))
                        if res7 == 0:
                                os.system('cls')
                        if res7 == 1:
                                break
                        os.system('cls')

                else:
                        print('[- ALUGAR -] Dê uma olhada em nosso portifólio.\n')

                        mostrar_lista_de_carros(carros)
                        print('')

                        linha()
                        alugar = int(input('Escolha o código do carro: \n'))
                        diaria = int(
                                input('Insira a quantidade de dias que deseja alugar: \n'))
                        os.system('cls')

                        print('Você escolheu {} por {} dias.'.format(
                                carros[alugar][0], diaria))
                        print('O aluguel totalizaria R$ {}. Deseja algugar? \n\n'.format(
                                carros[alugar][1]*diaria))

                        linha()
                        res2 = int(input('0 - SIM | 1 - NÃO\n'))
                        if res2 == 0:
                                os.system('cls')
                                print('Parabens você alugou o {} por {} dias.\n'.format(
                                carros[alugar][0], diaria))
                                alugueis.append(carros.pop(alugar))
                                linha()

                        res3 = int(input('0 - CONTINUAR | 1 - SAIR\n'))
                        if res3 == 0:
                                os.system('cls')
                        if res3 == 1:
                                break

        elif res == 2:
                os.system('cls')

                if len(alugueis) == 0:
                        print('Não existem carros para serem devolvidos!\n')
                        linha()
                        res6 = int(input('0 - CONTINUAR | 1 - SAIR\n'))
                        if res6 == 0:
                                os.system('cls')
                        if res6 == 1:
                                break

                        os.system('cls')
                else:
                        print('Segue a lista de carros alugados. Qual carro foi devolvido? \n')
                        mostrar_lista_de_carros(alugueis)
                        print('\n\n')

                        res4 = int(input('Escolha o código do carro que deseja devolver: '))
                        print('Obrigado por Alugar conoscos, o carro {} foi devolvido e pode ser alugado novamente.\n'.format(alugueis[res4][0]))
                        carros.append(alugueis.pop(res4))

                        linha()
                        res5 = int(input('0 - CONTINUAR | 1 - SAIR\n'))
                        if res5 == 0:
                                os.system('cls')
                        if res5 == 1:
                                break
        
        elif res == 3:
                os.system('cls')
                break


