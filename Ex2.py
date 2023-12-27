def numbers_between_a_and_b(a, b):
    if a < b:
        print("Ошибка: A должно быть меньше B.")
        return
    print(f"Целые числа между {a} и {b} (включая сами числа):")
    for number in range(a, b + 1):
        print(number, end=" ")
    count = b - a + 1
    print(f"\nКоличество чисел между {a} и {b}: {count}")
try:
    A = int(input("Введите значение A: "))
    B = int(input("Введите значение B: "))
except ValueError:
    print("Ошибка: Пожалуйста, введите целые числа.")
else:
    numbers_between_a_and_b(A, B)