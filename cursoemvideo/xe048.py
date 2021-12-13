soma = 0
cont = 1
for c in range(0, 501):
    if (c % 3) == 0 and (c % 2) != 0:
        soma = c + soma
        cont = cont + 1
        print(c)
print(f'multiplos de 3 impares são {cont} numeros que somam {soma}')
