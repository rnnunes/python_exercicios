
print('=== TUPLAS ===')

contagem_ext = ('Zero', 'Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
'Onze','Doze','Treze','Quatorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
cont_num = len(contagem_ext)

while True:
    questao = int(input('Digite um número entre 0 e 20: '))
    if  0 <=  questao <= 20:
        break

print('Voçê digitou o numero {}'.format(contagem_ext[questao]))
