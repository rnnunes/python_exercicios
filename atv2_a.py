from math import sqrt,hypot

print('====='*15)
oposto = float(input('Para fazer a formula de pitagoras, informe a valor do Cateto Oposto:\n'))
adjacente = float(input('Informe o valor do cateto adjacente:\n'))

hipotenusa = oposto**2 + adjacente**2
#hipotenusa = math.hypot(oposto, adjacente) esse é o certo kdjakdfjaksd

print('===='*15)
print('Se o cateto oposto for {:.2f} e o cateto adjacente for {:.2f}. Portanto o comprimento da hipotenusa é {:.2f}\n'.format(oposto ,adjacente ,sqrt(hipotenusa)))
print(' Agulos:\n Seno: {:.5f}\n Cosseno: {:.5f}\n Tangente: {:.5f}'.format(oposto/hipotenusa, adjacente/hipotenusa, oposto/adjacente))

print('===='*15)
