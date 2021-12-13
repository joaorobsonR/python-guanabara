pessoas = []
dados = []
maior = menor = 0

while True:
    dados.append(str(input('nome: ')))
    dados.append(int(input('peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if maior < dados[1]:
            maior = dados[1]
        if menor > dados[1]:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = str(input('deseja continuar? [s/n]'))
    if resp == 'n':
        break

print(f'foram {len(pessoas)} cadastradas')
print(f'o maior peso foi {maior}. Peso de ', end='')
for i in pessoas:
    if i[1] == maior:
        print(f'[{i[0]}] ', end='')
print()
print(f'o menor peso foi {menor}. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
