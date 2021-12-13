a = int(input('Digite o primeiro termo: '))
r = int(input('digite a razão: '))
q = int(input('digite a quantidade de termos da PA: '))
cont = 0
while cont < q:
    n = a + (cont) * r
    cont += 1
    print('->{} '.format(n), end='')
print('fim')
