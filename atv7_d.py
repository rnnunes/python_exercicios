print('=== GERADOR DE PA ===')

primeiro_termo = int(input('Primeiro Termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro_termo
cont = 1

while cont <= 10:
    print('P.A: {}'.format(termo))
    termo += razao
    cont += 1
print('Acabou!')