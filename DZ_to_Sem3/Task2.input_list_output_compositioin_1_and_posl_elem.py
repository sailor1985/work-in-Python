# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

import math

length = int(input("Введите количество чисел в списке: "))
num_list= []
num_list1= []
for i in range(length):
    element = int(input(f"Введите {i+1}-й элемент списка: "))
    num_list.append(element)
print(f"Заданный список следующий: \n {num_list}")

for i in range(int(math.ceil(length/2))):
    element1 = num_list[i] * num_list[length - 1 - i]
    num_list1.append(element1)
print(f"Итоговый список следующий: \n {num_list1}")