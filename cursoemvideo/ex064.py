def troco():
    print('-'*20)

troco()
soma = 0
n = int(input('digite 999 para parar '))
while n != 999:
    soma += n
    troco()
    n = int(input('digite 999 para parar '))
print('a soma dos termos digitados é {}'.format(soma))
print('fim')
