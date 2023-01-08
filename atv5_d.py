
print("===0"*15)

n1 = float(input('Informe a primeira nota do aluno: '))
n2 = float(input('Informe a segunda nota do aluno: '))
media =  (n1 + n2) / 2
if media < 5:
    print('Reprovado')
elif 6.9 > media >= 5:
    print('Recuperação')
else:
    print('Aprovado')