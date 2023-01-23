
def titulo(texto):
    print('='*30)
    print((texto))
    print('='*30)

def area(a, b):
    terreno = a * b
    print(f'A área de um terreno de {a} x {b} é de {terreno}m².')


titulo('FUNÇOES')
print('')
area(float(input('LARGURA (m): ')), float(input('ALTURA (m): ')))