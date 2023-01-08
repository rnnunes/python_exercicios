

print('===='*3 +' Loja ' + '===='*3)
print('')

vlr = float(input('Valor total do prduto: '))
comando = int(input('Selecione a forma de pagamento:\n 0 = Dinheiro/Cheque \n 1 = A vista no Cartão \n 2 = Parcelado no Cartão \n'))

if comando == 2:   
    print('Quantas Vezes deseja pagar?')
    print('3 = ate 2x no cartão')
    print('4 = 3x ou mais')
    cartão = int(input())

    if cartão == 3:
        print('O produto saiu pelo valor normal')

    elif cartão == 4:
        print('O produto saiu com "20%" de Juros, o valor final é R${:.2f}.'.format(vlr + ((vlr * 20) / 100)))
    

if comando == 0:
    print('O senhor tem "10%" de desconto no pagamento a vista dinheiro ou cheque. \n O produto ira sair por R${:.2f}.'
    .format(vlr - (vlr * 10) / 100))
elif comando == 1:
    print('O senhor tem "5%" de desconto no pagamento a vista dinheiro ou cheque. \n O produto ira sair por R${:.2f}.'
    .format(vlr - (vlr * 5) / 100))
        
