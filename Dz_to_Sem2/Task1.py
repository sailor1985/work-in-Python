# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44

number = input(f'Введите число N\n В случае ввода вещественного числа используйте ".": ')

number_split = number.split(".")
number_int = int(number_split[0]) # выделение целой части
number_float = int(number_split[1]) # выделение дробной части

def sum_of_digits(n): #функция нахождения суммы цифр в числе
    sum = 0
    while n != 0: 
        sum += n % 10
        n //= 10 
    return sum

sum_int = sum_of_digits(number_int)   #нашли суммы цифр в целой части числа
sum_float = sum_of_digits(number_float)   #нашли суммы цифр в дробной части числа
sum_finish = sum_int + sum_float   #общая суммы цифр в числе
print(f"Сумма цифр в числе {number} равна {sum_finish}")