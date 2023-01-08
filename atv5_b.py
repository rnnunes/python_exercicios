
num1 = int(input('Insira o primeiro numero a ser comparado: '))
num2 = int(input('Insira o segundo numero a ser comparado: '))

if num1 > num2:
    print('O primeiro valor é maior')
elif num2 > num1:
    print('O segundo valor é maior')
else:
    print('Não existe valor maior, os dois são iguais')