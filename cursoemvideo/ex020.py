import random

n1 = str(input('digite o nome: '))
n2 = str(input('digite o nome: '))
n3 = str(input('digite o nome: '))
n4 = str(input('digite o nome: '))
nome = [n1, n2, n3, n4]
random.shuffle(nome)
print('A ordem que vai ser apresentado o trabalho é ')
print(nome)
