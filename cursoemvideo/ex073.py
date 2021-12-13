tabela_Bra = ('são paulo', 'internacional', 'atletico-mg', 'flamengo', 'gremio', 'palmeiras', 'fluminense',
              'corinthians', 'santos', 'ceara', 'atletico-go', 'atletico-pr', 'bragantino', 'vasco', 'sport',
              'fortaleza', 'bahia', 'goias', 'botafogo', 'coritiba')

print(f'tabela dos times do brasilerão: {tabela_Bra}')
print(f'os quatro primeiros são {tabela_Bra[0:5]}')
print(f'os quatro ultimos são {tabela_Bra[16:]}')
verifica = str(input('digite um time para saber sua colocação: ')).strip().lower()
for pos, time in enumerate(tabela_Bra):
    if time == verifica:
        print(f'o {verifica} está na posição {pos+1}')

print(f'o palmeiras está na {tabela_Bra.index("palmeiras")+1} posição')
