


print('='*25)

lista = []

while True:
    num =int(input('Insira um novo valor: '))

    if num not in lista:
        lista.append(num)
        print('Numero cadastrado com sucesso.')
    else:
        print('Esse numero já foi cadastrado, o msm não sera duplicado.')

    comando = input('Deseja continuar? [S/N]').upper().split()[0]
    while comando not in 'SN':
        comando = input('Deseja continuar? [S/N]').upper().split()[0]
    if comando in 'N':
        break
        
print('Voce colocou os seguintes valores {}'.format(sorted(lista)))