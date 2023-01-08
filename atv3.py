
#frase= 'Curso Python'
#print(len(frase.replace('Python', 'Sir Rian')))
#print('Curso' in frase)
#dividido = frase.split()
#print(dividido[0])

print('====='*15)
nome = input('Insira o seu nome completo: \n').strip

print('Seu Nome é {}'.format(nome.upper()))
print('Seu Nome é {}'.format(nome.lower()))

cortar = nome.split()
print('Quantidade de letras(Não contanto espaçamentos) {}'.format(len(nome.replace(' ','')))) # (len(nome) - nome.count(' ')) tambem era possivel
print('Quantidade de letras no primeiro nome: {}'.format(len(cortar[0])))