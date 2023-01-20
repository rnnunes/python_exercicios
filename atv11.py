

print('=== INCOMPLETO ===')

nome_peso = []
final = []
maior = 0
menor = 0
cont = 0
while True:
    nome_peso.append(str(input('Insira o nome: ')).strip())
    nome_peso.append(float(input('Insira o peso: ')))

    if len(nome_peso) == 0:
        maior = menor = nome_peso[1]
    else:
         if nome_peso[1] > maior:
              maior = nome_peso[1]
         if nome_peso[1] < menor:
            menor = nome_peso[1]

    final.append(nome_peso[:])
    nome_peso.clear
    cont += 1

    comando = str(input('Deseja cadastrar mais pessoas? [SIM/NÃO]')).strip().upper()
    while comando not in 'SIMNÃONAO':
        comando = str(input('Deseja cadastrar mais pessoas? [SIM/NÃO]')).strip().upper()
    if comando in 'NÃONAO': 
            break

print('Lista total foi {}'.format(final))
print('O numero todal de individuos cadastrados é {}'.format(cont))
print('O maior peso foi {}Kg'.format(maior))
print('O menor peso foi {}Kg'.format(menor))