import random

print(random.random())
print(random.randint(0, 9))
#
from math import sqrt, ceil

n = int(input('digite um numero: '))
raiz = sqrt(n)
print(f'A raiz quadrada do numero é {raiz:.2f}, ou {ceil(raiz)} ')
