a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
cont = 0
while cont < 10:
    n = a + cont*r
    cont += 1
    print('-> {} '.format(n), end='')
print('pausa')
res = int(input('Deseja continuar? '))
if res != 0:
    while res != 0:
        for c in range(cont, (cont + res)):
            n = a + cont*r
            cont += 1
            print('-> {} '.format(n), end='')
        print('pausa')
        res = int(input('Deseja continuar? '))
print('O total de termos solicitados foi de {} termos'.format(cont))
print('\033[32mfim')
