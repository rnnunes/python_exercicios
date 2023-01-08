 
import sys

print('== PROGRESSÃO ARITÉTICA - 10 PRIMEIROS TERMOS ==\n')

pri_termo = int(input('Informe o primeiro Termo: '))
razao = int(input('Informe a Razão da P.A: '))
decimo = pri_termo + (10) * razao

for cont in range(pri_termo,decimo,razao):
    print(cont, end=" ")

