

print('===='*15) 
num = int(input('Digite um numero entre 0 a 9999:\n'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('===='*15)
print('O numero fica: \n Milhar: {} \n Centena: {} \n Dezena: {} \n Unidade: {}'.format(m, c, d, u))
