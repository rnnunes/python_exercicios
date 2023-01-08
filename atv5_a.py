

print('==='*15)
valor = int(input('Insira o valor a ser convertido: '))

print('Selecione a base de converção do valor inserido: \n 1 - Binario \n 2 - Octal \n 3 - hexadecimal\n')
comando = int(input())

if comando == 1:
    print('O valor selecionado em Binario é {}'.format(bin(valor))) 
elif comando == 2:
    print('O valor selecionado em octal é {}'.format(oct(valor)))
elif comando == 3:
    print ('O valor selecionado em hexadecimal é {}'.format(hex(valor)))