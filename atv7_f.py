
print('=== SEQUENCIA DE FIBONACCI ===')


n = int(input('Quantos termos você deseja mostrar? '))
f1 = 0
f2 = 1
cont = 3

print('{} - {} -'.format(f1,f2), end= '')
while cont <= n:
    f3 = f2 + f1
    print(' {} - '.format(f3), end= '')
    f1 = f2
    f2 = f3
    cont += 1


