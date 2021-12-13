n = float(input('digite um numero: '))
m = float(input('digite outro numero: '))
s = n + m
su = n - m
mu = n * m
p = n ** m
d = n / m
di = n // m
r = n % m
print('a soma é: {}, a subtração é: {}, a multiplicação é: {}'.format(s, su, mu), end='')
print(' a potencia é: {}, a divisão é: {}, divisão inteira é: {} e o resto é: {}'.format(p, d, di, r))

#escreva o nome
a = input('digite seu nome ')
b = input('digite o sobre nome ')
print('é um prazer em conhecer {:*>20} . {:*<20}'.format(b, a))
