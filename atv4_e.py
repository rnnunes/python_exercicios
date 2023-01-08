

print('==='*15)

num01 = int(input('Informe o primeiro numero: '))
num02 = int(input('Informe o segundo numero: '))
num03 = int(input('Informe o terceiro numero: '))

ordem = sorted([num01, num02, num03])

print('O menor numero é {} e o maior é {}'.format(ordem[0],ordem[2]))