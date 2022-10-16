# 5. Задайте число. Составьте список чисел Фибоначчи, в том числе
# для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# Примечание:
# Алгоритм смотрим тут: https://ru.wikipedia.org/wiki/Негафибоначчи
# Вам понадобится рекурсивный вызов функции или сделайте в виде списка.

# n = int(input("Введите число: "))

# x1 = [1,1]
# for i in range(0, n-2):
#     x1.append(x1[-1] + x1[-2])
# print(','.join(str(y) for y in x1))

# x2 = [-1, 1]
# for i in range(-3, n-2):
#     x2.append(x2[-1] - x2[-2])
#     #x2.reverse()
# print(','.join(str(y) for y in x2))

n = int(input('Введите длину ряда: '))
result1 = [1, 1]
result2 = []
f1 = f2 = 1

for i in range(0, n-2):
    f1, f2 = f2, f2 + f1
    result2.append(f2)
print(result2, end=' ')
print("\n")

for i in range(0, n+1):
    f1, f2 = f2, f1 - f2
    result1.append(f2)
result1.reverse()
print(result1, end=' ')
result1.extend(result2)
print("\n")
print(result1, end=' ')
print("\n")