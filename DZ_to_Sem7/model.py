import view
from texttable import Texttable
from prettytable import PrettyTable


def write_to_file(lst: str, filename):  # Запись в текстовый файл. Вход:строка
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(lst)


# def rewrite_to_file(string, filename):  # Дозапись в текстовый файл. Вход:строка
#     with open(filename, mode="a", encoding="utf-8") as file:
#         file.write(f"{string}\n")


def read_data(filename: str) -> list:  # Чтение из текстового файла. Вход:строка. Выход:список
    with open(filename, "r", encoding="utf-8") as data:
        a = data.read().split(", ")
    return a


def create_record(value_tup: tuple) -> str:  # Добавление записи (Фамилия, Имя, Телефон, Описание) в строковую переменную
    value_str = ", ".join(value_tup)
    return value_str


# def rendering_list(dic: dict): #Функция вывода на экран (в консоль) всех записей
#     table = Texttable()
#     # for i in range(len(dic)):
#     #     table.add_rows([["Фамилия", "Имя", "Телефон", "Описание"], dic[i]])
#     #     print(table.draw())
#     #     return dic

#     # for i in dic.values():
#     #     print(i)
#     #     table.add_rows([["Фамилия", "Имя", "Телефон", "Описание"], dic.values()])
#     # print(table.draw())
#     # return dic

#     # table = PrettyTable()

#     for key in dic.values():
#         print(key)
#         # table.add_rows(["Фамилия", "Имя", "Телефон", "Описание"], key[0:4])
#         # print(table.draw())
#     # print(table)

# print(rendering_list(struct_dic(2)))

# def rendering_random_dic(dictinary: dict): #Функция рисование поля клеток с отображением
#                                            #рандомного текущего состояния (frontend в консоли)
#     lst = list(dictinary.values()) #Вытащили из словаря все значения в список
#     table = Texttable()
#     # for i in range(len(lst)):
#     #     table.add_rows([["Фамилия", "Имя", "Телефон", "Описание"], lst[i][0], lst[i][1], lst[i][2], lst[i][3]])
#     #     print(table.draw())
#     print(lst)
#     print(lst[0][1])
# rendering_random_dic(struct_dic(2))
