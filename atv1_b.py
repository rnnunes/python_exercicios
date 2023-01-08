import math
#from math import sqrt, floor, ceil # importação apenas de coisas individuais da biblioteca
print('==*=='*15)
print('Olá, infome um numero:')
resposta = int(input())

dobro = resposta * 2
triplo = resposta * 3
raiz = math.sqrt(resposta) #novo metodo kakaka
print('')
print('O numero infomado foi {}, o Dobro é {}, o Triplo é {} e a raiz quadrada é {:.2f}.'.format(resposta, dobro, triplo, raiz))