#importaçoes

import random
import os

#variaveis

movimentos = ['Pedra', 'Papel', 'Tesolra']
jogador_cont = 0
computador_cont = 0


#funçoes

def linha():
    print('=============================')

def main_print():
    linha()
    print('\nPLACAR')
    print('Você: {}'.format(jogador_cont))
    print('Computardor: {}'.format(computador_cont))
    print('')
    print('Escolha seu Lance:')
    print('0 - Pedra │ 1 - Papel │ 2 - Tesoura')

def selecao_movimentos():
    return random.choice(movimentos)


def movimento_jogador():
    while True:
        try:
            jogada_usuario =int(input())
            if jogada_usuario not in [0, 1, 2]:
                raise
            return movimentos[jogada_usuario]
        
        except Exception as e:
            raise


def vencedor(jogada_jogador, jogada_computador):
    global computador_cont, jogador_cont, movimentos

    if jogada_jogador == 'Papel':
        if jogada_computador == 'Pedra':
            jogador_cont +=1
            return 'J'
        elif jogada_computador == 'Tesolra':
            computador_cont +=1
            return 'C'
        else:
            return 'E'
        
    if jogada_jogador == 'Pedra':
        if jogada_computador == 'Tesolra':
            jogador_cont +=1
            return 'J'
        elif jogada_computador == 'Papel':
            computador_cont +=1
            return 'C'
        else:
            return 'E'
        
    if jogada_jogador == 'Tesolra':
        if jogada_computador == 'Papel':
            jogador_cont +=1
            return 'J'
        elif jogada_computador == 'Pedra':
            computador_cont +=1
            return 'C'
        else:
            return 'E'
            

#programa principal

print('Bem Vindo ao Jogo de Pedra, Papel e Tesolra')
linha()
print('')

repetir = 1
while repetir == 1:
    main_print()
    jogada_jogador = movimento_jogador()
    jogada_computador = selecao_movimentos()
    placar = vencedor(jogada_jogador, jogada_computador)

    print('')
    linha()
    print('Sua Jogada: {}'.format(jogada_jogador.capitalize()))
    print('Jogada do computador: {}'.format(jogada_computador.capitalize()))

    if vencedor == 'J':
        print('Você Venceu!')
    elif vencedor =='C':
        print('Você Perdeu!')
    elif vencedor == 'E':
        print('Empate!')
    linha()

    while True:
        next = int(input('Jogar novamente? 0 - SIM │ 1 - NÃO\n'))
        if next == 0:
            break
        elif next == 1:
            repetir = 0
            break

    os.system('cls')

