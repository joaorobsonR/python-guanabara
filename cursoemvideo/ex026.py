frase = str(input('Digite a frase: ')).upper().strip()
print('A quantidades de A que aparece na frase é {}'.format(frase.count('A')))
print('O primeiro A que aparece na frase está na posição {}'.format(frase.find('A')+1))
print('O ultimo A que aprece na frase está na posição {}'.format(frase.rfind('A')+1))
