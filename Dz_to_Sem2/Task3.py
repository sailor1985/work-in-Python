# 3. Задайте список из n чисел последовательности (1+1/n)**n и
# выведите на экран их сумму.
# Пример:
# - Для n=4 [2, 2.25, 2.37, 2.44]
# Сумма 9.06

num = int(input('Введите количество чисел в последовательности, N: '))
num_list = []

for i in range(num+1):
   if i!=0: 
    num_list.append(round((1+1/i)**i, 2))
 
print(num_list)
sum = sum(num_list)
print(sum)