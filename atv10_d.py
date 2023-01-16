

lista_total = []
lista_impar = []
lista_par = []

while True:
    lista_total.append(int(input('Insira um valor: ')))

    comando = input('Deseja inserir mais valores [S/N]: ').upper().strip()[0]
    while comando not in ('SN'):
        comando = input('Deseja inserir mais valores [S/N]: ').upper().strip()[0]
    if comando in 'N':
        break



print('Todos os valores digitados: {}.\n'.format(lista_total))
'''print('Todos os valores pares digitados: {}.\n'.format(lista_par))
print('Todos os valores impares digitados {}.\n'.format(lista_impar))
'''