listaOrdenada = []
l = []
for c in range(0, 5):
    n = int(input('digite um valor: '))
    listaOrdenada.append(n)

for i in range(0, len(listaOrdenada)):
    l.append(min(listaOrdenada))
    listaOrdenada.remove(min(listaOrdenada))

print(l)

lista = []
for x in range(0, 5):
    m = int(input('digite um valor: '))
    if x == 0 or m > lista[-1]:
        lista.append(m)
        print('adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if m <= lista[pos]:
                lista.insert(pos, m)
                print(f'adicionado na posição {pos}')
                break
            pos += 1
print('-=-'*20)
print(f'a lista com os valores ordenados é {lista}')
