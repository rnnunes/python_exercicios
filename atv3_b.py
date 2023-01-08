

print('==='*15)
print('=='*6 + ' Informe sua cidade ' + '=='*6)
print('==='*15)

resp = str(input('Vamos verificar se sua cidade começa com o nome "SANTO": ')).strip().upper().split()

print('A cidade informada {}, começa com "SANTO"? {}.'.format(resp, 'SANTO' in resp[0]))