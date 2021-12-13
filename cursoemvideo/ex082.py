l = []
lpar = []
limpar = []
while True:
    n = int(input('digite um valor: '))
    l.append(n)
    resp = str(input('deseja continuar? '))
    if resp in 'Nn':
        break

for c in l:
    if c % 2 == 0:
        lpar.append(c)
    else:
        limpar.append(c)

print(f'a lista completa é {l}')
print(f'os numeros pares da lista são {lpar}')
print(f'os numeros impares da lista são {limpar}')
