
print('==='*15)
sal = float(input('Olá Proletariado, Informe o seu salario atual:\n'))

new_sal = sal + ((sal * 15) / 100)

print('======'*5)
print('Olá Sr. Proletariado, Parabens o senhor ganhou um reajuste de 15% na sua remuneração', end='')
print('a mesma esta atualmente em R${} Reais \n mas a partir de agora é R${:.2f} Reais,'.format(sal, new_sal))