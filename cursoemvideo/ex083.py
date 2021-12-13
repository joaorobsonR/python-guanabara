lista = []
ex = str(input('digite uma expressão matematica: '))
for c in ex:
    if c == '(':
        lista.append('(')
    elif c == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('sua expressão é valida')
else:
    print('sua expressão é invalida')



