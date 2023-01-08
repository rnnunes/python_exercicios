import random

print('=== Jogo Advinhação ===')
adv = int(input('Insira um numero de 0 a 10 e tente adivinhar: '))
computador = random.randint(0,10)
cont = 1

while adv != computador:
    adv = int(input('Infelimente vc errou, tente novamnete: '))
    cont += 1
    if computador > adv:
        print('Um pouco mais...')
    elif computador < adv:
        print('Menos...')

print('Parabens vc acerdou, o numero correto era {}'.format(computador))
print('Vc precisou de {} tentativas.'.format(cont))