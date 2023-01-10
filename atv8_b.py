import random

print('=== JOGO PAR OU IMPAR ===')

cont = 0
while True:
    computer = random.randint(0,10)
    print(computer)

    
    num = int(input('Insira um valor: '))
    comando = input('Par ou Impar? [P/I]').strip().upper()[0]
    cont += 1
    
    if comando == 'P':
        soma = computer + num
        if soma % 2 == 0:
            print('Você Ganhou, Colocou {} e o computador colocou {}, a soma dos dois fica {}.'
            .format(num, computer, soma))
        else:
            print('Você Perdeu, Game Over! Vc Colocou {} e o computador colocou {}, a soma dos dois fica {}.'
            .format(num, computer, soma))
            break

    if comando == 'I':
        soma = computer + num
        if soma % 2 == 1:
            print('Você Ganhou, Colocou {} e o computador colocou {}, a soma dos dois fica {}.'
            .format(num, computer, soma))
        else:
            print('Você Perdeu, Game Over! Vc Colocou {} e o computador colocou {}, a soma dos dois fica {}.'
            .format(num, computer, soma))
            break
    


print('GAME OVER! Você venceu {}x.'.format(cont))
print('==='*15)
