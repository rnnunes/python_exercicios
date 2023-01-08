

print('==='*15)
vlr_casa = float(input('Informe o valor da casa que deseja financiar: '))
vlr_sal = float(input('Informe o valor do seu salario: '))
qtd_parcelar = int(input('Em quantos anos deseja pagar: '))

meses_parcela = qtd_parcelar * 12
max_porc = (vlr_sal * 30) / 100
tempo_meses = vlr_casa/max_porc

if tempo_meses <= meses_parcela: 
    print('Parabens seu emprestimo foi aprovado!')
else:
    print('Infelizmente seu emprestimo não pode ser aprovado.')    