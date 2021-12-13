from random import randint
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'os valores da lista são {n}')
print('o maior valor sorteado é ', max(n))
print('o menor valor sorteado é ', min(n))

from random import sample
a = tuple(sample(range(10), 5))
print(a)
print(f'O maior valor é {max(a)} e o menor é {min(a)}.')
