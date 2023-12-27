A = int(input('Введите значение A: '))
B = int(input('Введите значение B: '))
summ = 0
summ_2 = 0
summ_1 = 0
for i in range(A, B + 1):
    summ += i
    if i % 2 == 0:
        summ_2 += i
    else:
        summ_1 += i
print(f"""Сумма чисел от {A} до {B} = {summ}
Сумма четных чисел от {A} до {B} = {summ_2}
Сумма нечетных чисел от {A} до {B} = {summ_1}""")