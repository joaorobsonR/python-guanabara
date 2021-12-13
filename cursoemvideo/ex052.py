cont = 0
n = int(input('Digite um numero: '))
for c in range(1, n+1):
    if n % c == 0:
        print('\033[32m', end=' ')
        cont += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
if cont == 2:
    print('\n\033[mO numero digitado é primo foi dividido duas vezes')
else:
    print('\n\033[mO numero digitado não é primo foi dividido mais que duas vezes')
