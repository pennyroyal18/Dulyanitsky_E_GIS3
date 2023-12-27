price = float(input('Введите цену за 1 кг конфет: ').replace(',', '.'))
for i in range(2, 11, 2):
    print(1 + i/10, 'кг стоит', round(price + price * i/10, 2))