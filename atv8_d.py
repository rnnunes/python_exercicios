

print('=== LEITOR DE NOMES E PREÇOS ===')

soma = cont = cont1k = menor = 0

while True:
    nome = input('Insira o nome do produto: ').split()
    valor = int(input('Insira o valor do produto: '))

    soma += valor
    cont += 1

    if valor > 1000:
        cont1k += 1
    
    comando = input('Deseja continuar a cadastrar produtos? [S/N]').upper().split()[0]
    while comando not in 'SN':
        comando = input('Deseja continuar a cadastrar produtos? [S/N]\n').upper().split()[0]
    if comando in 'N':
        break

print('==='*15)
print('Total da compra {}'.format(soma))
print('Apenas {} produtos custando mais de R$ 1000 Reais'.format(cont1k))
print('')
