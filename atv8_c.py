

print('=== VERIFICADOR ===')

cont = 0
total = 0
masc = 0
femin = 0
genero =''
comando = ''


while True:

    idade = int(input('Informe a sua idade: '))
    genero = input('Informe o seu Genero: [M/F]').upper().strip()[0]
    while genero not in 'MF':
        genero = input('Informe o seu Genero: [M/F]').upper().strip()[0]
    cont += 1


    if idade >= 18:
        total +=1 

    if genero == 'M':
        masc += 1
    
    if genero == 'F' and idade < 20:
        femin += 1
    

    comando = input('Deseja continuar o cadastro? [SIM/NÃO]').upper().strip()
    while comando not in 'SIMNÃONAO':
        comando = input('Deseja continuar o cadastro? [SIM/NÃO]').upper().strip()
    if comando in 'NAONÃO':
            break


print('''        1) Quantidade de pessoas com mais de 18 anos igual: {}.
        2) Quantidade de homens foram cadastrados: {}.
        3) Quantas Mulheres tem menos de 20 anos: {}.'''.format(total, masc, femin))

print('O total de pessoas cadastradas foi {}, Mulheres:  e Homens: '.format(cont))