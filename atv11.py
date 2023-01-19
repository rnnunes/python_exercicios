

print('==='*15)

nome_peso = []
final = []
cont = 0

while True:
    nome_peso.append(str(input('Insira o nome: ')).strip())
    nome_peso.append(float(input('Insira o peso: ')))
    final.append(nome_peso[:])
    nome_peso.clear
    cont += 1

    comando = str(input('Deseja cadastrar mais pessoas? [SIM/NÃO]')).strip().upper()
    while comando not in 'SIMNÃONAO':
        comando = str(input('Deseja cadastrar mais pessoas? [SIM/NÃO]')).strip().upper()
    if comando in 'NÃONAO': 
            break

print('O numero todal de individuos cadastrados é {}'.format(cont))
print(final)