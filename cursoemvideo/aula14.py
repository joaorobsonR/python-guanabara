n = 1
r = 'SIM'
par = impar = 0
while r == 'SIM':
    print('Digite Três numeros')
    for c in range(0, 3):
        n = int(input('Digite um numero: '))
        if n % 2 == 0:
            par += +1
        else:
            impar += +1
    r = str(input('Deseja continuar? ')).upper().strip()
print('você digitou {} numeros pares e {} numeros impares.'.format(par, impar))
