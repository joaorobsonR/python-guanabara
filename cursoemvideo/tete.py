'''
def l(x):
    soma = 0
    for i in x:
        soma+= i
    return soma

lista = []
while len(lista) != 5:
    lista.append(int(input('digite um numero: ')))

print(lista)
print(l(lista))
print(sum(lista))
'''

li = [10,2,36,5,48,15]
def ordem(x):
    a= []
    for i in x:
        a.append(min(x))

    return a

print(ordem(li))
