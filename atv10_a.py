

('=== LISTAS ===')


lista = []
maior = 0
menor = 0

for c in range(0,5):
    lista.append(input('Insira um novo valor {}°:'.format(c)))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

print('Maior valor foi {} na posição '.format(maior), end='')
for i, v in enumerate(lista):
    if v == maior:
        print('{}...'.format(i), end='')
print('')

print('Menor valor foi {} na posição '.format(menor), end='')
for i, v in enumerate(lista):
    if v == menor:
        print('{}...'.format(i), end='')