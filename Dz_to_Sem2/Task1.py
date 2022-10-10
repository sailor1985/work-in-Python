# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44

number = float(input(f'Введите число N: '))

def sum_of_digits(n):
    sum = 0
    while n != 0: 
        sum += n % 10
        n //= 10 
    return sum

sum_digits = int(sum_of_digits(number))
print(f"Сумма цифр в числе {number} равна {sum_digits}")