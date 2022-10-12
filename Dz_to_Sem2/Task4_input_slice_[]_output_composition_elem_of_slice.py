# 4. Задайте список из элементов, заполненных числами из промежутка [-N, N].
# Задайте два числа - позиции(индексы) в исходном списке это границы диапазона.
# Найдите произведение элементов списка в указанном диапазоне индексов
# Пример:
# N = 6
# Пример списка чисел: [-2, -5, 4, 1, 4, 1, 2, -5, -3, 0, -6, -6, 5]
# границы диапазона: 2, 5
# Произведение для [4, 1, 4, 1] равно 16

# Примечание: Границы диапазона вводятся пользователем, надо корректно учесть,
# что они могут быть некорректными: больше длины списка, меньше нуля, первый
# больше второго и т.п.

import random, functools

N = int(input('\nЗадайте N - верхнюю и нижнюю границу промежутка чисел [-N, N], \nиз которого будут браться элементы для включения в список: '))
num_list_in_range = list(range(-N, N+1))
print(f"\nНабор чисел из промежутка от -{N} до {N} для составления из них списка элементов:\n {num_list_in_range}")

num_list_random_sampling = random.choices(num_list_in_range, k=2*N+1)
print("\nСписок чисел: ", num_list_random_sampling)

while True:
    left_slice = input('Задайте левый срез (индекс списка) : ')
    right_slice = input('Задайте правый срез (индекс списка) : ')
    if not left_slice.isnumeric() and not right_slice.isnumeric():
        print("Не корректный ввод данных.Вы ввели не число. Попробуйте снова:: ")
    elif not len(num_list_random_sampling) <= int(left_slice) < 0 and len(num_list_random_sampling) <= int(right_slice) < 0 :
        print("Ваше число вне диапазоне. Попробуйте снова")
    else:
        print("\nЧисла в правильном диапазоне.")
        break

y = slice(left_slice, right_slice + 1)
print(f"\nC учетом левого среза {left_slice} и правого среза {right_slice} \nИтоговый список чисел: ", num_list_random_sampling[y])

x = functools.reduce(lambda a, b : a * b, num_list_random_sampling[y])
print(f"Произведение чисел в списке, отображенном выше, равно {x}")