
from random import randint

print('=== TUPLAS ===')

num = (randint(0,10),randint(0,10),randint(0,10),randint(0,10),randint(0,10))

ordem = sorted(num)

print('Numeros gerados randomicamente: {}.'.format(num))
print('Menor numero gerado {}, Maior numero gerado {}'.format(min(ordem),max(ordem)))