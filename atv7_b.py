
import time
print('=== Maios ou menso uma calculadora ===')

num1 = float(input('Informe o primeiro valor:'))
num2 = float(input('Informe o segundo valor: '))

comando = 0
while comando != 5:
    print('''    [1] - SOMA
    [2] - MULTIPLICAR
    [3] - MAIOR 
    [4] - NOVOS NUMEROS
    [5] - SAIR DO PROGRAMA''')

    comando = int(input('Insira um comando do Menu: '))

    if comando == 1:  
        print('A Soma dos valores é {}.\n'.format(num1 + num2))
    elif comando == 2:
        print('A Multiplicação dos valores é {}.\n'.format(num1 * num2))
    elif comando == 3:
        if num1 > num2:
            print('O maior numero entre os dois é {}.\n'.format(num1))
        else:
            print('O maior numero entre os dois é {}.\n'.format(num2))
    elif comando == 4:
        print('Ok, escolher novos numeros.\n')
        num1 = float(input('Informe o primeiro valor:'))
        num2 = float(input('Informe o segundo valor: '))
    elif comando == 5:
        print('Finalizando...')
        time.sleep(2)
    else:
        print('Comando invalido!')
    
print('Fim do programa.')
time.sleep(3)