
preço =  float(input('Informe o preço do produto:\n'))

Valor_final = preço - ((5 * preço) / 100)

print('O valor infomado foi de R${} Reais, seu novo preço com descondo de 5% é de R${:.2f} reais.'.format(preço,Valor_final))