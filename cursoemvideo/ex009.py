n = int(input('tabuada do numero: '))
for count in range (11):
    print(f'{n:^2} x {count+0:^2} = {n*(count+0):^2}')

#como o professor que com o print('*'*12) para dar um efeito
m = int(input('tabuada do numero: '))
print('*'*12)
print(f'{m:^2} x 0  = {m*0:^2}')
print(f'{m:^2} x 1  = {m*1:^2}')
print(f'{m:^2} x 2  = {m*2:^2}')
print(f'{m:^2} x 3  = {m*3:^2}')
print(f'{m:^2} x 4  = {m*4:^2}')
print(f'{m:^2} x 5  = {m*5:^2}')
print(f'{m:^2} x 6  = {m*6:^2}')
print(f'{m:^2} x 7  = {m*7:^2}')
print(f'{m:^2} x 8  = {m*8:^2}')
print(f'{m:^2} x 9  = {m*9:^2}')
print(f'{m:^2} x 10 = {m*10:^2}')
print('*'*12)
