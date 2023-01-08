
print('='*40)
print(f'{"NUMEROS PRIMOS":^40}')
print('='*40)

num = int(input('Insira um numero: '))
cont = 0

for x in range(1,num+1):
    if num % x == 0:
        print('\033[33m', end=' ')
    else:
        print('\033[31m', end=' ')
    cont =+ 1
    print(x)

print('Contador {}'.format(cont))