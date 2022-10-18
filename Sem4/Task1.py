#Задайте строку из набора чисел
#Напишите программу, которая покажет большее именьшее число
#В качестве символа разделите используйте пробел

#Усложнение: создайте строку чисел через случайные числа
#Подсказка: используйте метод строки Join

from random import randint

# my_str = "12 34 -11 9894 4373 123 -1"
# my_str = my_str.split()
# print(my_str)
# print(max(my_str), min(my_str))

#Усложнение
num =[]
for i in range(10):
    num.append(str(randint(-10, 10)))
print(str(num))

res1 = " ".join(num)
print(res1)
res2 = res1.split()
print(res2)
print(max(res2), min(res2))