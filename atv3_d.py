


print('====='*10)

frase = input('Escreva uma Frase: \n').strip().upper()

print('A seu Frase Possui {} letras "A", a primeira vez q ela aparece e na posição {} e ulitma na posição {}'
.format(frase.count('A'), frase.find('A')+1, frase.rfind('A')+1))