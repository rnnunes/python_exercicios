print('=== GERADOR DE PA V3 ===')

primeiro_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
cont = 1
total = 0
mais_num = 10

while mais_num != 0:
    total += mais_num
    while cont <= total:
        print('P.A: {}'.format(termo))
        termo += razao
        cont += 1
    print('Esperar')
    mais_num = int(input('Quantos termos a mais vc deseja ver? '))

print('Foram verificados {}'.format(total))
print('Acabou!')