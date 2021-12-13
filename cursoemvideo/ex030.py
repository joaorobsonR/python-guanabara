n = int(input('Digite um numero '))
if (n%2) == 0:
    print(f'O numero digitado \033[1;32m{n}\033[m é par!')
else:
    print('O numero digitado \033[1;31m{}\033[m é impar!'.format(n))
