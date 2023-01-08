

frase = str(input('Digite uma frase: ')).upper().strip()
words = frase.split()
junto = ''.join(words)
inverso = ''

for letras in range(len(junto) - 1,-1,-1):
    inverso += junto[letras]
    
if junto == inverso:
    print('Esta frase é um palindromo {}'.format(inverso))
else:
    print('Infelizmente essa frase não é um palindromo')