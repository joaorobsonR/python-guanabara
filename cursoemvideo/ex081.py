l = []
while True:
    n = int(input('digite um valor para lista: '))
    l.append(n)
    while True:
        resp = str(input('deseja continuar? ')).lower().strip()
        if resp in 'sn':
            break
    if resp == 'n':
        break

print(f'foram digitados um total de {len(l)} valores')
l.sort(reverse=True)
print(f'a lista na ordem decresente é {l}')
if 5 in l:
    print('o numero 5 está presente na lista')
else:
    print('o numero 5 não está presente na lista')
print(l)
