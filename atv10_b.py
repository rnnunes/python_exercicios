


print('='*25)

lista = []

while True:
    lista.append(int(input('Insira um novo valor: ')))
    print('Valor adicionado com sucesso...')

    comando = input('Deseja continuar? [S/N]').upper().split()[0]
    while comando not in 'SN':
        comando = input('Deseja continuar? [S/N]').upper().split()[0]
    if comando in 'N':
        break
        
print('Voce colocou os seguintes valores {}'.format(sorted(lista)))