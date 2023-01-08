

print('===='*16)
print('LER 6 NUMEROS E MOSTRAR SÓ OS QUE FOREM PAR, SE FOR IMPAR NÃO MOSTRAR')
print('===='*16)
print('')

soma = 0

for num in range(1,7):
    ler_comando = int(input('Insira o {}º numero a ser verificado: \n'.format(num)))
    if ler_comando%2 == 0:
        soma = soma + ler_comando

print('O Resultado da soma de todos os numeros PARES inserios são: {}.'.format(soma))