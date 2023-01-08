

print('=== TABUADA 2.0 ===')

num = int(input('Insira o numero que deseja saber a tabuada do 1 a 10:'))

for x in range(1,10+1):
    print('{}x {:2} = {}'.format(num,x,num*x))

print('=='*15)