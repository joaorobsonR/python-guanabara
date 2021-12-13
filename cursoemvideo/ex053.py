frase = str(input('Digite uma frase: ')).strip().upper().split()
nfrase = ''.join(frase)
inverso = nfrase[::-1]
if nfrase == inverso:
    print(nfrase, inverso)
    print('temos um palindromo')
else:
    print(nfrase, inverso)
    print('não temos um palindromo')
