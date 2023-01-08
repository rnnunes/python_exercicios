print('===='*10)
alt = float(input('Olá, Infome a altura em metros da parete:\n'))
comp = float(input('Informe o comprimento em metros da parete:\n'))

area = alt * comp
litros = area / 2
print('Area da parade em questão {} metros, então sera nescessario {} litros de tinta para pintar.'.format(area, litros))