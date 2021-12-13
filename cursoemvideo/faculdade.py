n = int(input('Quantas temperaturas serão lidas? '))
s = c = cont = 0
while cont < n:
    if n > 0:
        t = int(input('Digite a temperatura: '))
        if t > 0:
            s = s + t
            c += 1
        else:
            print('N tem que ser maior que 0')
    cont += +1
print('A media das temperaturas é {}'.format(s/c))
