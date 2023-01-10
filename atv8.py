

print('=== FLAG BREAK ===')

cont = soma = 0

while True:
    num = int(input('Insira um valor: (999) Stop'))
    if num == 999:
        break
    cont += 1
    soma += num
print('Foram {} e soma de todos eles é {}.'.format(cont, soma))