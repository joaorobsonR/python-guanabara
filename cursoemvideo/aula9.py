frase = 'Curso em Vídeo Python'
print(frase)
print(frase[9]) #para fatiar um caracter forma mais simples
print(frase[9:14]) #para fatiar do 9 ao 14 excluindo o ultimo
print(frase[0:21:2]) #para fatiar pulando em 2 por exmplo
print(frase[:5]) #omite o zero
print(frase[15:]) #do 15 até o final por exemplo quando quer ir até o final da frase
print(frase[9::3]) #do 9 até o final pulando de 3 em 3

#analise
print(len(frase)) #conta a quantidade de caracteres
print(frase.count('o')) #conta a quantidade de letra entre ''
print(frase.count('o', 0, 13)) #count com fatiamento
print(frase.find('deo')) #encontra o deo no texto por exemplo, obs encontra onde começa
print('Curso' in frase) #retorna True or False
