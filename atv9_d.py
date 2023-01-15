

print('='*60)
print(f'{"TABELA DE PREÇOS - ESSE AQUI É LEGAL":^50}')
print('='*60)

tabela = ('Refrigerante', 5, 
            'Pão', 2, 
            'Pneu', 400,
            'Maçarico', 200)

for pos in range(0, len(tabela)):
    if pos %2 == 0:
        print(f'{tabela[pos]:.<30}', end='')
    else:
        print(f'R${tabela[pos]:>7.2f}')
