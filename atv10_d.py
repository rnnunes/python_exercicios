
 

lista_total = []
lista_par = []
lista_impar = []


while True:
    lista_total.append(int(input('Insira um valor: ')))

    comando = input('Deseja inserir mais valores [S/N]: ').upper().strip()[0]
    while comando not in ('SN'):
        comando = input('Deseja inserir mais valores [S/N]: ').upper().strip()[0]
    if comando in 'N':
        break

for p, c in enumerate(lista_total):
    if c % 2 == 0:
        lista_par.append(c)
    elif c % 2 ==1:
        lista_impar.append(c)


print('Todos os valores digitados: {}.\n'.format(lista_total))
print('Todos os valores pares digitados: {}.\n'.format(lista_par))
print('Todos os valores impares digitados {}.\n'.format(lista_impar))
