print('\033[32mVERIFICANDO A CONSIÇÃO DE EXISTENCIA\033[m')
a = int(input('Digite o lado a do tringulo: '))
b = int(input('Digite o lado b do tringulo: '))
c = int(input('Digite o lado c do tringulo: '))
if abs(b-c) < a and a < (b+c):
    print('A condião de existencia é verdadeira a={}, b={}, c={}'.format(a, b, c))
else:
    print('\033[31mEsse triângulo é impossível')
