#TUPLAS

lanche = ('hamburgue', 'suco', 'pizza', 'pudim', 'batata')

print(lanche[-3])
print(lanche[2:])
print(lanche[:2])

for comida in lanche:
    print(f'eu comi {comida}')
print('comi pra caramba!\n')

for c in range(0, len(lanche)):
    print(f'eu comi {lanche[c]}')
print('comi pra caramba!')

for cont in range(0, len(lanche)):
    print(cont)

for pos, i in enumerate(lanche):
    print(f'eu vou comer {i}, na posição {pos}')

print(sorted(lanche)) #coloca na ordem a tupla, mas não altera

a = (1,2,3)
b = (2,4,6,8)
c = a + b
print(c)

print(c.count(2))
print(c.index(4))

del(c)

