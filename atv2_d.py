import random

print('==='*15)
aluno1 = input('Olá Professor! Insira o nome do primeiro aluno:')
aluno2 = input('Insira o nome do segundo aluno:')
aluno3 = input('Insira o nome do terceiro aluno:')
aluno4 = input('Insira o nome do quarto aluno:\n')

lista_de_alunos = (aluno1,aluno2,aluno3,aluno4)

print('==='*15)
print('O Aluno sorteado para limpar o quadro é o {}. kkk sfdeu'.format(random.choice(lista_de_alunos)))