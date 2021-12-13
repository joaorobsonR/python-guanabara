s = cont = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    s += n
    cont += 1

print('a soma dos numeros digitados é {}'.format(s))
print((f'a quantidade de numeros digitados é {cont}'))
