n1 = float(input('Digite um numero '))
n2 = float(input('Digite um numero '))
n3 = float(input('Digite um numero '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print('O maior numero digitado é o {}'.format(maior))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O menor numero digitado é o {}'.format(menor))
