import os
while True:
  operadores = {"+", "-", "*", "/"}

  print('='*20)
  n1 = int(input('Digite um Numero:'))
  print('')
  n2 = int(input('Digite um Numero:'))
  print('='*20)
  print('')
  print('Soma vale {}'.format(n1 + n2), end=" pipi")
  print("sou foda")

  print('Deseja continuar a fazer calculos, Sim ou Não')
  comando = input()
  if comando == "Não":
    break  