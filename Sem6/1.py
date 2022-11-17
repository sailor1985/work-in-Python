''''Задача 41. Напишите программу вычисления арифметического выражения заданного строкой.
Возможные операции в выражении только: +,-,/,*. приоритет операций стандартный.
Техническое задание:
1) Числа могут быть только целые, любой размерности
2) Унарный оператор минус не рассматриваем, т.е. '-2*3' недопустимо
3) Не используйте функцию eval.
4) Программа возвращает результат вычисления в виде числа.
Общая схема решения:
1) Выделить части алгоритма, использовать для них функции.
2) Протестировать функции на множестве примеров, убедиться в правильности работы. Создать "модуль тестирования".
Пример:
2+2 -> 4
1+2*3 -> 7
1-2*3 -> -5
1-2*33 -> -65
2-1+3*7 -> 10
1-2*3/5 -> -0.2
1+2*3-6*5+78 -> 55'''

# Парсинг строки. (строка) -> (список)
def parsing(my_str):
    new_list = []
    temp = 0
    for idx,elem in enumerate(my_str):
        if elem in "+-/*":
            new_list.append(int(my_str[temp:idx]))  # добавили 1 temp = 0
            new_list.append(elem) # добавили "+" в new_list
            temp = idx + 1 #индекс "+"
    new_list.append(int(my_str[temp:]))

    return new_list

new_list = [1, '+', 2, '*', 3, '/', 6]  #parsing
# На входе parse список - new_list , на выходе - число

def run(new_list):
    temp = 0
    tmp_list = new_list.copy()
    length = len(tmp_list)
    idx = 0

    while idx < length:
        elem = tmp_list[idx]
        if elem == '*':
            temp = tmp_list[idx-1] * tmp_list[idx+1]
            tmp_list[idx] = temp
            tmp_list.pop(idx + 1)
            tmp_list.pop(idx - 1)
            length -= 2
        elif elem == '/':
            temp = tmp_list[idx-1] / tmp_list[idx +1]
            tmp_list[idx] = temp
            tmp_list.pop(idx + 1)
            tmp_list.pop(idx - 1)
            length -= 2
        else: idx += 1

    length = len(tmp_list)
    idx = 0

    while idx < length:
        elem = tmp_list[idx]
        if elem == '+':
            temp = tmp_list[idx - 1] + tmp_list[idx + 1]
            tmp_list[idx] = temp
            tmp_list.pop(idx + 1)
            tmp_list.pop(idx - 1)
            length -= 2
        elif elem == '-':
            temp = tmp_list[idx - 1] - tmp_list[idx + 1]
            tmp_list[idx] = temp
            tmp_list.pop(idx + 1)
            tmp_list.pop(idx - 1)
            length -= 2
        else:
            idx += 1

    return tmp_list[0]


my_str = "1+2*3-6*5+78"
print(run(parsing(my_str)))








