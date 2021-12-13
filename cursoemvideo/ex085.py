from random import  randint

numeros = [[], []]
cont = 0
while True:
    numero = randint(0, 10)
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)
    cont += 1
    if cont == 7:
        break
print(numeros)
numeros[0].sort()
numeros[1].sort()
print(f'os numeros pares digitados foram {numeros[0]}')
print(f'os numeros impares digitados foram {numeros[1]}')
