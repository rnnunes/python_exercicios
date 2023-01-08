

print('==='*15)
sal = int(input('Informe o seu salario atual: '))

if sal > 1250:
    print('Seu salario sofreu um reajuste de 10%, agora ele é R$ {:.2f}.'.format(sal + ((sal * 10) / 100)))
elif sal <= 1250:
    print('Seu salario sofreu um reajuste de 15%, agora ele é R$ {:.2f}.'.format(sal + ((sal * 15) / 100)))