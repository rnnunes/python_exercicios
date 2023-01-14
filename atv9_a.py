

tabela = ('PAL', 'INT','FLU','COR','FLA','CAP','CAM','FOR','SAO','AMG','BOT',
'SAN','GOI','RBB','CFC','CUI','CEA','AGO','AVA','JPFC')

print('Os 5 primeiros times do Futebol: {}'.format(tabela[:5]))
print('Os quatro ultimos colocados da tabela são: {}'.format(tabela[17:]))
print('A Tupla em ordem alfabetica fica: \n{}'.format(sorted(tabela)))
print('O Time Ji-parana Futebol Clube esta em {}° posição na tabela kk'.format(tabela.index('JPFC')+1))