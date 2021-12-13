tupl = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
while True:
    n = int(input('digite um numero entre 0 e 20: '))
    if n in tupl:
        print(f'voce digitou o numero {n}, que está na posição {tupl.index(n)}')
    if n == 999:
        break
    else:
        print('numero não encontrado, digite novamente!')

print('\033[31mFIM\033[m')

cont = ('zero' ,'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze',
        'quize', 'dezeseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    m = int(input('digite um numero entre 0 e 20: '))
    if m >= 0 and m <= 20:
        print(f'voce digitou o numero {cont[m]}')
    elif m < 0 or m > 20:
        print('numero digitado não encontrado, tente novamente!')

    while True:
        resp = str(input('deseja continuar [S/N]?')).strip().upper()
        if resp == 'S' or resp == 'N':
            break
    if resp == 'N':
        break


