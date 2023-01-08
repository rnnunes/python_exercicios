import random
import time


print('==='*8)
print('==== Jogo da Velha ====')
print('==='*8)
print('')

comando = input('Escolha o comando: \n  Tesolra \n  Papel \n  Pedra \n').strip().upper()

time.sleep(1)
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PO!!')
time.sleep(1)

listaMovimentos = ['PEDRA','PAPEL','TESOLRA']
Pc_Escolha = random.choice(listaMovimentos)

if comando == "TESOLRA" and Pc_Escolha == "PAPEL":
    print('Parabens, voçê ganhou!, eu havia escolhido {}.'.format(Pc_Escolha))
elif comando == "TESOLRA" and Pc_Escolha == "PEDRA":
    print('Infelizmente, vc Perdeu!! havia escolhido {}'.format(Pc_Escolha))
elif comando == "TESOLRA" and Pc_Escolha == "TESOLRA":
    print('Empatamos, havia escolhindo {}.'.format(Pc_Escolha))

if comando == "PAPEL" and Pc_Escolha == "PEDRA":
    print('Parabens, voçê ganhou!, eu havia escolhido {}.'.format(Pc_Escolha))
elif comando == "PAPEL" and Pc_Escolha == "TESOLRA":
    print('Infelizmente, vc Perdeu!! havia escolhido {}'.format(Pc_Escolha))
elif comando == "PAPEL" and Pc_Escolha == "PAPEL":
    print('Empatamos, havia escolhindo {}.'.format(Pc_Escolha))

if comando == "PEDRA" and Pc_Escolha == "TESOLRA":
    print('Parabens, voçê ganhou!, eu havia escolhido {}.'.format(Pc_Escolha))
elif comando == "PEDRA" and Pc_Escolha == "PAPEL":
    print('Infelizmente, vc Perdeu!! havia escolhido {}'.format(Pc_Escolha))
elif comando == "PEDRA" and Pc_Escolha == "PEDRA":
    print('Empatamos, havia escolhindo {}.'.format(Pc_Escolha))
else:
    print('Comando Inválido')