

expressao = str(input('Digite a expressão: '))

pilha = []
for simb in expressao:
    if simb    == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break

if len(pilha) == 0:
    print('Sua expressão esta válida')
else:
    print('Sua expressão esta errada')