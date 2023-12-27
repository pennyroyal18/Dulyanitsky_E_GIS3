def get_numerical_word(val: int) -> str:
    chisla = ["один", "два", "три", "четыре", "пять","шесть", "семь", "восемь", "девять", "десять","одиннадцать", "двенадцать"]
    if 1 <= val <= 12:
        return chisla[val - 1]
    else:
        return ""

if __name__ == "__main__":
    try:
        user_input = int(input("Введите целое число от 1 до 12: "))
        result = get_numerical_word(user_input)
        if result:
            print(f"{user_input}: {result}")
        else:
            print("Число вне диапазона от 1 до 12.")
    except ValueError:
        print("Ошибка: Пожалуйста, введите целое число.")