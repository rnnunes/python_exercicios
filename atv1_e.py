print('**'*15)
print('Informe o numero para ser verificada a tabuada:')
n1 = int(input())

tabuada = (n1*1, n1*2, n1*3, n1*4, n1*5, n1*6, n1*7, n1*8, n1*9, n1*10)
print('')
print('Segue tabuada do numero {} ate o multiplo de 10'.format(n1))
print('{}x1 = {:2}'.format(n1 ,n1*1)) # tbm poderia ser assim kakaaka
print('{}x2 = {:2}'.format(n1, tabuada[1]))
print('{}x3 = {:2}'.format(n1, tabuada[2]))
print('{}x4 = {:2}'.format(n1, tabuada[3]))
print('{}x5 = {:2}'.format(n1, tabuada[4]))
print('{}x6 = {:2}'.format(n1, tabuada[5]))
print('{}x7 = {:2}'.format(n1, tabuada[6]))
print('{}x8 = {:2}'.format(n1, tabuada[7]))
print('{}x9 = {:2}'.format(n1, tabuada[8]))
print('{}x10 = {:2}'.format(n1,tabuada[9]))
print('=='*15)