soma = 0
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
for n in range(0, 10):
    soma = a1 + (n)*r
    print('->{}'.format(soma), end=' ')
print('\033[32mFIM\033[m')
