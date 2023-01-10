

print('=== MAIOR E MENOR VALOR ===')

cont = soma = 0
res = 'S'
lista = []

while res in 'S':
    num = int(input('Digite um numero: '))
    cont += 1
    soma += num
    res = input('Quer continuar? [S/N]').strip().upper()[0]
    lista.append((num))

print('Voce digitou {} numeros e a media foi {}.'.format(cont, soma/cont))
print('O maior valor digitado foi {} e o menor foi {}.'.format(max(lista),min(lista)))