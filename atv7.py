

print('== =='*10)

genero =  input('Informe seu genero: [M/F]').upper().strip()[0]

while genero not in 'MF':
    genero = input('Dados inválidos. Por favor, informe seu genero corretamente [F/M]:').strip().upper()[0]
print('Genero {} registrado com sucesso.'.format(genero))