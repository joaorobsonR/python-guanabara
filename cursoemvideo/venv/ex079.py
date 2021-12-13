listaPessoal = []
while True:
    n = int(input('Digite um numero: '))
    if n in listaPessoal:
        print('já tem esse valor na lista, não irei adicionar!')
    else:
        print('valor adicionado com sucesso! ')
        listaPessoal.append(n)
    while True:
        resp = str(input('Deseja continuar[s/n]? ')).strip().lower()
        if resp == 'n' or resp == 's':
            break
    if resp == 'n':
        break

listaPessoal.sort()
print('-=-'*20)
print(f'os valores digitados são {listaPessoal}')
