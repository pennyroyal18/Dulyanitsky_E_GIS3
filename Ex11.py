def simple_or_not():
    num = int(input('Введите число, которое хотите проверить: '))
    if num / num == 1  and num == num:
        print('True')
    else:
        print('False')
    return num
if __name__ == '__main__':
    simple_or_not()