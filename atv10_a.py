

('=== LISTAS ===')


lista = []

for c in range(0,5):
    lista.append(input('Insira um novo valor {}°:'.format(c)))

for pos, cont in enumerate (lista):
    print('Posição {} Valor {}'.format(pos, cont))

print('Maior valor foi {} na posição {}.'.format(max(lista), pos), end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print('{}...'.format(i), end='')
print('')

print('Menor valor foi {} na posição {}.'.format(min(lista)), end='')
