

print('==='*15)

reta1 = float(input('Infome o tamanho da primeira reta: '))
reta2 = float(input('Informe o tamanho da segunda reta: '))
reta3 = float(input('Informe o tamnho da terceira reta: '))

if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
    print('As Retas informadas podem formar um Triangulo!')
    if reta1 == reta2  == reta3:
        print('Ira formar um triangulo Equilatero!') #podia de colocado esse no else kakakak
    elif reta1 == reta2 or reta2 == reta3 or reta3 == reta1:
        print('Ira formar um Triagulo Isóceles')
    elif reta1 != reta2 != reta3 != reta1:
        print('Ira formar um triangulo Escaleno')
else:
    print('Infelizmente não é possivel formar um triangulo com essas retas.')
