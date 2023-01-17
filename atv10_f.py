

#esse eu não entendi 100%

lista = []

for c in range (0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)

    else:
        pos = 0 
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1 

print('Valores na ordem sem o uso do Sort, Lista {}'.format(lista))