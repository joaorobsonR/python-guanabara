import math

x = float(input('digite o cateto adjacente '))
y = float(input('digite o cateto oposto '))
a = math.hypot(x, y)
print(f'o valor da hipotenusa é {a}')

#caulculo no broço
co = float(input('digite o cateto oposto '))
ca = float(input('digite o cateto adjacente '))
hip = co*co + ca*ca
hipo = math.sqrt(hip)
print(f'a hipotenusa é {hipo}')

#agora usando o cosseno
cosseno = float(input('digite o angulo do cosseno '))
cateto = float(input('digite o tamanho do cateto '))
hipotenusa = cateto/math.cos(math.degrees(cosseno))
print(f'o valor da hipotenusa é {hipotenusa}')

print(f'cosseno de {cosseno} é {math.cos(math.radians(cosseno))}')

#usando o seno
seno = float(input('digite o angulo do seno '))
catsen = float(input('digite o tamanho do cateto '))
hipotsen = catsen/math.sin(math.degrees(seno))
print(f'o valor da hipotenusa é {hipotsen}')
