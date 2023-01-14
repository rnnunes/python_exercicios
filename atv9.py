
print('=== TUPLAS ===')

contagem_ext = ('Zero', 'Um','Dois','Três','Quatro','Cinco',
                'Seis','Sete','Oito','Nove','Dez','Onze',
                'Doze','Treze','Quatorze','Quinze','Dezesseis',
                'Dezessete','Dezoito','Dezenove','Vinte')


while True:
    questao = int(input('Digite um número entre 0 e 20: '))
    if  0 <=  questao <= 20:
        print('Voçê digitou o numero {}'.format(contagem_ext[questao]))

        comando = input('Voce deseja continuar a verificar numeros [S/N]').upper().split()[0]
        while comando not in 'SN':
             comando = input('Voce deseja continuar a verificar numeros [S/N]').upper().split()[0]
        if comando in 'N':
            break
