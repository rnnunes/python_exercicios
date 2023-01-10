

print('=== LEITURA DE VARIOS VALORES COM WHILE ===')

num = cont = soma = 0

num = int(input('Insira um numero: '))
while num != 999:
        cont += 1
        soma += num
        num = int(input('Insira um numero: '))

print(f'A soma de todos os numeros foi {soma} com {cont} numeros digitados.')
print('Acabou')