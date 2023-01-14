

print('=== T U P L A S - NOVAMENTE ===')



num = (int(input('Insira o primeiro valor: ')),
    int(input('Insira o segundo valor: ')),
    int(input('Insira o terceiro valor: ')),
    int(input('Insira o quarto valor: ')))


print('Voce digitou os seguintes numeros: {}'.format(num))
print('O numero de vezes que o 9 apareceu foi {}x'.format(num.count(9)))
if 3 in num:
    print('A primeira posição do numero 3 é {}°'.format(num.index(3)+1))
else:
    print('O valor 3 não foi digitado em nenhuma solução')

for n in num:
    if n% 2 == 0:
        print('Os valores digitados pares são {}'.format(n))