import math
def taxi(km):
    distance = km * 1000
    add_price = distance / 140
    f_price = 240 + (add_price * 15)
    return(round(f_price, 2))
print(f"Стоимость вашей поездки {taxi(float(input('Введите расстояние поездки в километрах: ').replace(',', '.')))} рублей.")