

import random
import time
import operator

jogo = {'Player 01': random.randint(1,6),
        'Player 02': random.randint(1,6),
        'Player 03': random.randint(1,6),
        'Player 04': random.randint(1,6)}

ranking = []
print('Valores Sorteados:')

for k, v in jogo.items():
    print('{} Tirou {} no dado.'.format(k, v))
    time.sleep(1)
print('')

ranking = sorted(jogo.items(), key=operator.itemgetter(1), reverse=True)
print(ranking)
print('')

print('-== RANKING ==-')
for i, v in enumerate(ranking):
    print('{} lugar: {} com {}.'.format(i+1, v[0], v[1]))
    time.sleep(1)