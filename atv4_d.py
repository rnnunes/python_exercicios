import calendar

ano = int(input('Qual ano deseja verificar se é bissesto: \n'))

if calendar.isleap(ano) == True:
    print('O Ano {} foi Bissesto!'.format(ano))
else:
    print('o Ano {} não é bissesto.'.format(ano))