

print('===='*15)
vel = float(input('Qual a velocidade do carro? (Km/h) '))

if vel > 80: 
    print('Voce foi multado por excesso de velocidade, sua velocidade esta acima de 80Km/h!')
    print('Sua Multa é de R$ {:.2f} Reais, sendo R$ 7.00 por KM acima da velocidade permitida.'.format((vel - 80) * 7.00))