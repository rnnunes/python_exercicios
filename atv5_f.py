
print('Bem Vindo a Calculador de IMC\n')

alt = float(input('Informe a sua Altura: '))
peso = float(input('Informe o seu peço: '))

imc = peso / (alt**2)

if imc < 18.5:
    print('Esta abaixo do peso')
elif 18.5 <= imc < 25: #pode ser assim: 18.5 <= imc < 25, sem o uso do and
    print('Peso ideal')
elif imc >= 25 and imc < 30:
    print('Sobrepeso')
elif imc >= 30 and imc < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')
print('{:.2f}'.format(imc))