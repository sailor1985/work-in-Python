# 3. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

my_list = [randint(1, 10) for i in range(randint(5, 10))]
print(f"\nЗадана следующая последовательность чисел: \n {my_list}\n" )
print(f"Cписок неповторяющихся элементов исходной последовательности:\n {set(my_list)}\n")