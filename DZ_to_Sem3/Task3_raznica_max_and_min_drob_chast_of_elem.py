# 3. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением
# дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01, 12.00] => 0.19
# Примечание:
# Обратите внимание на элемент 5 и и 12.0. Они не участвуют в процессе
# т.к. дробная часть ноль.
# В списке могут быть как числа float, так и числа int.
# Посмотрите на методы числа float, возможно пригодятся.

import math, functools

length = int(input("Введите количество чисел в списке: "))
num_list= []

for i in range(length):
    element = float(input(f"Введите {i+1}-й элемент списка: "))
    num_list.append(element)
print(f"Заданный список следующий: \n {num_list}")

float_list1 = list(filter(lambda x: not x % 2 == 0 and not x % 2 == 1, num_list))
print(f"Cписок ТОЛЬКО вещественных чисел следующий: \n {float_list1}")

float_list2 = list(map(lambda x: round(x % 1, 2), float_list1))
print(f"Cписок выделенных дробных частей вышеупомянутых вещественных чисел следующий: \n {float_list2}")

max_number = max(float_list2)
min_number = min(float_list2)
result = max_number - min_number
print(f"Максимальное число из списка следующее {max_number}")
print(f"Минимальное число из списка следующее {min_number}")
print(f"Разница между максимальным и минимальным числом равна {result}")