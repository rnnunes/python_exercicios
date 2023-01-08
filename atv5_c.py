import datetime

nascimento = int(input('Insira o ano do seu nascimento: '))
hj = datetime.date.today().year
idade = hj - nascimento

if idade < 18:
    print('Ainda não esta na hora de se alistar, ainda faltam {} anos.'.format(18 - idade))
elif idade > 18:
    print('Já passou o perido de alistamento há {} anos'.format(idade - 18))
elif idade == 18:
    print('Vc já pode se alistar')
print(idade)

