a = int(input('Digite o vaolor do lado A: '))
b = int(input('Digiteo o valor do lado B: '))
c = int(input('Digite o valor do lado C: '))
if a == b == c:
    print('Triãngulo EQUILATERO A={} B={} C={}'.format(a, b, c))
elif a == b or a == c or b == c:
    print('triângulo ISOCELES A={} B={} C={}'.format(a, b, c))
elif abs(b-c) < a and a < (b+c):
    print('Triãngulo ESCALENO A={} B={} C={}'.format(a, b, c))
else:
    abs(b-c) < a and a < (b+c) == False
    print('\033[31mExistencia IMPOSSÍVEL\033[m')
