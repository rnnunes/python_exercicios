import random
import time

lista = []
jogos = []

print('==== * MEGA SENA * ====\n')

quantt = int(input('Quantos jogos sera nescessario? '))
print('')
total = 1

while total <= quantt:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1

print('       --- NUMEROS ALEATORIOS --- \n --- {} JOGOS GERADOS RANDOMICAMENTE --- \n'.format(quantt))
for i, l in enumerate(jogos):
    time.sleep(1)
    print('Jogo {}: {}'.format(i, l))
