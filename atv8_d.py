

print('=== LEITOR DE NOMES E PREÇOS ===')

soma = cont = 0

while True:
    nome = input('Insira o nome do produto: ').split()
    valor = int(input('Insira o valor do produto: '))

    soma += valor
    cont += 1

    comando = input('Deseja continuar a cadastrar produtos? [SIM/NÃO]').upper().split()
    if comando in 'NÃONAO':
        break

print('Total da compra {}'.format(soma))
