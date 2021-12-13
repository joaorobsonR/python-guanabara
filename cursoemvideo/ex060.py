from math import factorial
n = int(input('Digite um numero: '))
fac = factorial(n)
for c in range(n, 1, -1):
    print('{} x '.format(c), end=' ')
print('1 = {}'.format(fac))
print('\033[32mFatorial de {} é {}\033[m'.format(n, fac))
