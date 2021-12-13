from random import randint

print('-='*20)
print('{:^40}'.format('JOGOS DA MEGASSENA'))
print('-='*20)
jogos = []
cont = 0
resp = int(input('quantos jogos vc quer fazer? '))
while cont != resp:
    while len(jogos) < 6:
        n = randint(1, 60)
        if n not in jogos:
            jogos.append(n)
        len(jogos)
    jogos.sort()
    print(jogos)
    jogos.clear()
    cont += 1
print('-='*20)
