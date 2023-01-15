


palavras_tab = ('aprender','programar','liguagem','estudar', 'praticar', 'trabalhar', 'futuro')

for palavra in palavras_tab:
    print('\nNa palavra {} temos '.format(palavra), end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')