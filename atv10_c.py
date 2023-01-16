
print('='*15)

lista = []

while True:
    lista.append(int(input('Insira um valor: ')))

    comando = input('Deseja continuar [S/N]').upper().split()[0]
    while comando not in 'SN':
        comando = input('Deseja contunar [S/N]').upper().split()[0]
    if comando in 'N':
            break

print('A quantidade de valores digitados foram {}.'.format(len(lista)))

print('A lista de valores digitados de forma decrescente {}'.format(sorted(lista, reverse=True)))
 
if 5 in lista:
    print('Existe o valor 5 na lista? Correto existe na posição {}.'.format(lista.index(5)))
else:
    print('Não existe o valor 5 na lista digitada')