

print('=== BOLETIN DE ALUNOS ===')

ficha = []
while True:

    nome = input('Insira o nome do aluno: ').capitalize().strip()
    n1 = float(input('Insira a 1° nota do aluno {}: '.format(nome)))
    n2 = float(input('Insira a 2° nota do aluno {}: '.format(nome)))
    media = (n1 + n2) / 2

    ficha.append([nome, [n1, n2], media])

    comando = str(input('Deseja inserir novos alunos? ')).upper().strip()
    while comando not in 'SIMNAONÃO':
        comando = str(input('O programa responderá apenas o comando de SIM OU NÃO, Por favor insira novamente: ')).upper()
    if comando in 'NÃONAO':
        break

print(f'{"N°.":<4}{"Nome":<10}{"Média":>8}')
print('-'*25)

for pos, n in enumerate(ficha):
    print(f'{pos:<4}{n[0]:<10}{n[2]:>8.1f}')

print('=='*30)
while True:
    comando2 = int(input('Mostrar notas de qual aluno? (999 para intenromper o programa)'))
    if comando2 == 999:
        print('Finalizando...')
        break
    if comando2 <= len(ficha) - 1:
        print('Notas de {} são {}'.format(ficha[comando2][0], ficha[comando2][1]))
