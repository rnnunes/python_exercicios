

print('=== SOMA TODOS OS NUMEROS IMPARES Q SÃO MULTIPLOS DE 3, DE 1 ATE 500')

soma = 0

for num in range(1,500,2):
    if num%3 == 0:
        soma =+ num 
        print(num)

print('')
print('Soma de dos numero: {}'.format(soma))