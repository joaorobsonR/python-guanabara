matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
maior = soma = soma3 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'digite um valor na posição [{l}][{c}]'))
print('-='*20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            soma3 += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        elif l == 1 and c <= 3:
            if matriz[l][c] > maior:
                maior = matriz[l][c]
    print()

print(f'a soma dos valores pares são {soma}')
print(f'o maior valor da segunda coluba é {maior}')
print(f'a soma da terceira coluna é {soma3}')
