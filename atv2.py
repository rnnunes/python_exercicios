from math import trunc

print('===='*15)
res = float(input('Informe um numero:'))

print('')
print('O numero {} tem parte interia {}.'.format(res, trunc(res))) # ou usar {:.0f} ou usar o int(num) ai pega só o valor inteiro da parada