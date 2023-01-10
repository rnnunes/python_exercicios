

print('=== VERIFICADOR ===')
cont = 0

while True:

    if genero != 'M' or genero != 'F':
        genero = input('Informe o seu Genero: [M/F]').upper().strip()[0]

    idade = int(input('Informe a sua idade: '))
    cont += 1

    

    comando = input('Deseja continuar o cadastro? [SIM/NÃO]').upper().strip()
    if comando in 'NAONÃO':
        break

print('O total de pessoas cadastradas foi {}, Mulheres:  e Homens: '.format(cont))