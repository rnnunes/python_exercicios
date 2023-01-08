
print('==='*15)
viagem = int(input('Qual a distancia da sua viagem em Km?'))

if viagem <= 200:
    print('Sua viagem vai ficar R${} Reais, sendo R$ 0.50 por Km ate 200Kms'.format(0.50 * viagem))
else:
    print('Sua viagem vai ficar R${} Reais, sendo R$ 0.45 devido a ser uma viagem longa.'.format(0.45 * viagem))