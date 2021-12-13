teste  = []
teste.append('isis')
teste.append('1')
familia = []
familia.append(teste[:])
teste[0] = 'joão'
teste[1] = 27
familia.append(teste[:])
print(familia)

galerinha = [['maria', 26], ['joão', 27], ['isis', 1]]
for p in galerinha:
    print(f'{p[0]} tem {p[1]} anos de idade')

rapaziada = list()
dados = []
for i in range(0, 3):
    dados.append(str(input('nome: ')))
    dados.append(int(input('idade: ')))
    rapaziada.append(dados[:])
    dados.clear()

print(rapaziada)

