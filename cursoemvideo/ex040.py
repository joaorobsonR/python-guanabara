n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
if media < 5:
    print('REPROVADO')
elif media >= 5 and media <6.9:
    print('RECUPERAÇÃO')
elif media >= 6.9 and media < 10:
    print('APROVADO')
else:
    print('Feliz 2020')
