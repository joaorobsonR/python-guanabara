tab = '\033[32mTABUADA\033[m'
while True:
    print('-=-'*10)
    print('{:^35}'.format(tab))
    print('-=-'*10)
    n = int(input('Digite um numero: '))
    if n < 0:
        break
    for c in range(0, 11):
        print('{:^2} x {:^2} = {:^2}'.format(c, n, (n*c)))

