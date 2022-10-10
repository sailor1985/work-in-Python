#13. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

str_scope = "123hgfd123jgdg1234ritrpr1"
str_find = "12"
# [MAIN] Основной вариант решения:

# 1. Ищем клады
print(f"Кол-во вхождений: {str_scope.count(str_find)}")

# 2. Изобретаем велосипеды
# [*] - Усложнение: Подумать об эффективности
# Что у нас внутри цикла
find_count = 0
for i in range(len(str_scope) - len(str_find) + 1):
    str_block = str_scope[i:i + len(str_find)]
    if str_block == str_find:
        find_count += 1
print(f"Кол-во вхождений: {find_count}")