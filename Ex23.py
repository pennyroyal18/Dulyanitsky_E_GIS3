def check_divisibility_by_seven(number):
   
    tens = (number // 10) * 3

    
    units = number % 10

    
    sum_result = tens + units

    
    if sum_result % 7 == 0:
        return f"{number} делится на 7 (по условию)"
    else:
        return f"{number} не делится на 7 (по условию)"


user_input = input("Введите число: ")

try:
    
    user_number = int(user_input)

    
    result = check_divisibility_by_seven(user_number)
    print(result)

except ValueError:
    print("Пожалуйста, введите целое число.")

#n = int(input('n = '))
#while n >= 10:
 #   d, e = divmod(n, 10)
  #  n = d*3 + e
#print(n == 7)#