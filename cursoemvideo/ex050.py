soma = 0
cont = 0
for n in range(1, 7):
    n = int(input('Digite o {} numero: '.format(n)))
    if (n % 2) == 0:
        soma = n + soma
        cont = cont+1
print('tatal da soma é ', soma, 'e os numeros pares são', cont)
