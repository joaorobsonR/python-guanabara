tabe_Preco = ('lapis', 1.70, 'borracha', 2.00, 'caderno', 15.70, 'estojo', 25.50,
              'tranferidor', 4.20, 'compasso', 5.00, 'mochila', 120.00, 'caneta', 2.00, 'livro', 10.00)

print('-'*40)
print(f'{"Tabela de Preço":^40}')
print('-'*40)

for pos in range(0, len(tabe_Preco)):
    if pos % 2 == 0:
        print(f'{tabe_Preco[pos]:.<30}', end='')
    else:
        print(f'R${tabe_Preco[pos]:>7.2f}')
print('-'*40)
