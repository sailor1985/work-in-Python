# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import functools

length = int(input("Введите количество чисел в списке: "))
num_list= []

for i in range(length):
    element = int(input(f"Введите {i+1}-й элемент списка: "))
    num_list.append(element)
    
print(f"Заданный список следующий: \n {num_list}")



# y = slice(left_slice, right_slice + 1)
x = functools.reduce(lambda a, b : a * b, num_list)
print(f"Произведение чисел в списке, отображенном выше, равно {x}")