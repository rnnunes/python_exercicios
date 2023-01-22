


aluno = {}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['media'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] <= 7:
    aluno['situação'] = 'Recuperação'
else: 
    print('Reprovado')

for k, v in aluno.items():
    print('{} é igual a {}'.format(k,v))
