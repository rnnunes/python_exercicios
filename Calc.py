import os

while True:
    os.system("clear")
    print("======================")
    print("0 : Soma")
    print("1 : Subtração")
    print("2 : Multiplicação")
    print("3 : Divisão")
    print("4 : Exponenciação\n")

    print("Escolha a operação que deseja realizar:")

    operação = int(input())

    if operação == 0:
        print("Operação escolhida Soma\n")
        print("---------------------------")
        print("Qual o primeiro valor:")
        n01 = int(input())
        print("Qual o segundo valor:")
        n02 = int(input())
        print("---------------------------")

        soma = n01 + n02
        print("Resultado {} + {} é igual a {}\n".format(n01, n02, soma))

    elif operação == 1:
        print("Operação escolhida Subitração\n")
        print("---------------------------")
        print("Qual o primeiro valor:")
        n01 = int(input())
        print("Qual o segundo valor:")
        n02 = int(input())
        print("---------------------------")

        sub = n01 - n02
        print("Resultado {} - {} é igual a {}\n".format(n01, n02, sub))

    elif operação == 2:
        print("Operação escolhida Multiplicação\n")
        print("---------------------------")
        print("Qual o primeiro valor:")
        n01 = int(input())
        print("Qual o segundo valor:")
        n02 = int(input())
        print("---------------------------")

        mult = n01 * n02
        print("Resultado {} x {} é igual a {}\n".format(n01, n02, mult))

    elif operação == 3:
        print("Operação escolhida Divição\n")
        print("---------------------------")
        print("Qual o primeiro valor:")
        n01 = int(input())
        print("Qual o segundo valor:")
        n02 = int(input())
        print("---------------------------")

        Div = n01 / n02
        print("Resultado {} / {} é igual a {:.2f}\n".format(n01, n02, Div))

    elif operação == 4:
        print("Operação escolhida Exponenciação\n")
        print("---------------------------")
        print("Qual o primeiro valor:")
        n01 = int(input())
        print("Qual o segundo valor:")
        n02 = int(input())
        print("---------------------------")

        Exp = n01 ** n02
        print("Resultado {} ^ {} é igual a {}\n".format(n01, n02, Exp))

    else:
        print("Valor incorreto, Por favor insira um valor contido na lista!\n")

    print("Deseja fazer uma nova conta? 0=Sim 1=Não")
    comando = int(input())
    if comando == 1:
        break
