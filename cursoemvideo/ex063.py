def fibite(n):
    if n < 2:
        return n
    else:
        res = fibite(n-1) + fibite(n-2)
        return res

def traco():
    print('--'*10)

traco()
termos = int(input('Digite quantos termos: '))
traco()
cont = 3
t1 = 0
t2 = 1
print('→ {} → {}'.format(t1, t2), end='')
while cont <= termos:
    t3 = t1 + t2
    print('→ {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' FIM')
traco()

print(fibite(8))
