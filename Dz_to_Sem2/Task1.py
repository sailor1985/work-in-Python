# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
# Пример:
# - 6782     -> 23
# - 0,56     -> 11
# - 187,6778 -> 44

number = float(input(f"Введите число N\n В случае ввода вещественного числа используйте точку: "))

str_number = str(number) # перевод из типа float в тип str
str_number = str_number.replace('.', '')  # производим замену десятичного разделителя
lst_str = list(str_number)   # перевод строки с числом в список строк с цифрами
lst_num = map(int, lst_str)   # преобразовываем каждый элемент полученного
                              # списка строк с цифрами в список целых чисел
sum_number = sum(lst_num)  # применяем функцию `sum()`
print(f"Сумма цифр в числе {number} равна {sum_number}")