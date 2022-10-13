# 20. Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.

str_list = ["qwe", "asd", "zxc", "12", "qwe", "ertqwe", ]
res = 0
find_str = "x"

for i in str_list:
    if find_str in i:
      res += 1

if res == 0:
    print("Элемент отсуствует в списке") 
else:
    print(f"Элемент {find_str} присутствует в списке {res} раз(а)")