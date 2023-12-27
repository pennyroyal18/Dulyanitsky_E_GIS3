A = float(input('Введите значение длины отрезка A: '))
B = float(input('Введите значение длины отрезка B: '))
count = 0
while A >= B:
    A -= B
    count += 1
print(f'Длина незанятой части отрезка A будет равна {count}')