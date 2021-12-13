num = [1,2,3,4]
num[3] = 5
num.append(6)
num.insert(0, 0)
num.sort(reverse=True)
num.pop(0)
if 4 in num:
    num.remove(4)
else:
    print('não achei o numero 4 na lista')
print(num)
print(f'essa lista tem {len(num)}')

from random import randint

l = []
for i in range(0, 11):
    l.append(randint(1, 20))

for c , v in enumerate(l):
    print(f'na posição {c}, encontrei o valor {v}')
print('cheguei ao final da lista')

a = [2,3,8,7]
b = a
print(a)
print(b)
b[2] = 6
print(a)
print(b)
x = [2,3,9,4]
y = x[:]
y[0] = 1
print(x)
print(y)
