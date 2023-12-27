A, B, C = int(input('Введите значение A: ')), int(input('Введите значение B: ')), int(input('Введите значение C: '))
C_A, C_B = 0, 0
x = 0
while A >= C:
    A -= C
    C_A += 1
while B >= C:
    B -= C
    C_B += 1
for i in range(C_B):
    x += C_A
print(f'{x} квадратов размещено на прямоугольнике')