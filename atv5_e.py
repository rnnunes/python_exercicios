import datetime

nascimento = int(input('Informe o ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - nascimento

if idade <= 9:
    print('Nadador Mirim')
elif idade > 9 and idade <= 14:
    print('Nadador Infantil')
elif idade > 14 and idade <= 19:
    print('Nadador Junior')
elif idade == 20:
    print('Nadador Sênior')
else:
    print('Nadador Master')