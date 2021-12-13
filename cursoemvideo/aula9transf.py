frase = '   Curso em Vídeo Python   '
print(frase.upper()) #todas maiuscula
print(frase.lower()) #todas minusculas
print(frase.capitalize()) #primeira letra da frase maiuscula
print(frase.title()) #todas as palavras com a primeira letra maiuscula
print(frase.strip()) #retira os espaços inuteis
print(frase.rstrip()) #retira os espaços inuteis à direita(right)
print(frase.lstrip()) #retira todos os espaços à esquerda(left)
print(frase.split()) #!!! divide o texto muito importante
print(frase.replace('Vídeo','streming')) #muda alguamas partes do texto
print('-'.join(frase)) #junta o texto

#zueirinha
frase = 'isis minha filha linda'
print(len(frase))
nova = frase.replace('linda', 'esperta')
print(len(nova))
dividido = frase.split()
print(dividido[2][1])
