

print('=== BANCO - CAIXA ELETRONICO - ERRO VERIFICAR - TEM Q MELHORAR ===')

saque = int(input('Que valor voçê quer sacar? R$: '))
total = saque
cedula = 50
cont_cedula = 0


while True:
    if total >= cedula:
        total -= cedula
        cont_cedula += 1
    else:
        if cont_cedula > 0:
            print('Total de Cedulas {}, Cedulas de R$ R$ {}.'.format(cont_cedula,cedula))
            if cedula == 50:
                    cedula = 20
            elif cedula == 20:
                cedula = 10
            elif cedula == 10:
                cedula = 1
            if total == 0:
                    break
