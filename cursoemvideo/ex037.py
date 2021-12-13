n = int(input('Digite o numero para ser covertido: '))
print('''\033[32mDigite 1 para converter para base decimal
Digite 2 para converter para base octal
Digite 3 para converter para base hexadecimal\033[m ''')
base = int(input('Digite a base escolhida '))
if base == 1:
    print('O numero {} na base decimal é {}'.format(n, bin(n)[2:]))
elif base == 2:
    print('O numero {} na base octal é {}'.format(n, oct(n)[2:]))
elif base == 3:
    print('O numero {} na base hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('\033[31mOpção inválida tente novamente\033[m ')


