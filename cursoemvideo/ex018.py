import math

c = float(input('digite um angulo para o cosseno '))
s = float(input('digite um angulo para o seno '))
t = float(input('digite o angulo da tangente '))
print(f'cosseno {math.cos(math.radians(c)):.3f} seno {math.sin(math.radians(s)):.3f} tangente {math.tan(math.radians(t)):.3f}')
#só de um angulo
a = int(input('digite o angulo '))
print(f'o seno {math.sin(math.radians(a)):.3f} o cosseno {math.cos(math.radians(a)):.3f} a tangente {math.tan(math.radians(a)):.3f}')
