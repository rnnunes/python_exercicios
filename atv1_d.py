print('xxx'*15)
print('Olá, Informe o valor em metros que sera convertido:')
resposta = int(input())

centimetros = resposta * 100
milimetros = resposta * 1000

print('')

print('{} metros são {} centrimetros, ou seja, {} milimetros.'.format(resposta, centimetros, milimetros))