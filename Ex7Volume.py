from math import pi
r = int(input('Введите значение Радиуса: '))
circle_area = round(pi*r**2, 3)
orb_vol = round(4/3*pi*r**3, 3)
print(f"Площадь круга с данным радиусом будет равна {circle_area},а объём шара  будет равен {orb_vol}")