print('{:=^50}'.format('\033[32mTABUADA\033[m'))
cont = 0
n = int(input('digite um numero para ver sua tabuada '))
for cont in range(-1, 10):
    r = (cont+1) * n
    print(f'{cont+1} x {n} = {r}')
print('fim')
print('='*43)
