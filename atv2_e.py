from random import shuffle

print('==='*15)
aluno1 = input('Olá Professor! Insira o nome do primeiro aluno para ser sorteado: ')
aluno2 = input('Insira o nome do segundo aluno: ')
aluno3 = input('Insira o nome do terceiro aluno: ')
aluno4 = input('Insira o nome do quarto aluno: ')

lista_de_alunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista_de_alunos)

print('===='*15)
print('A sequencia de alunos sorteados para fazer a apresentação:\n')
print(' Primeiro: {} \n Segundo: {} \n Terceiro: {} \n Quarto: {}'
.format(lista_de_alunos[0], lista_de_alunos[1], lista_de_alunos [2], lista_de_alunos[3]))
print('')