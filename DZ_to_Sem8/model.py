from texttable import Texttable
import csv


# Запись в текстовый файл. Вход: словарь
def export_to_file(filename: str, data: dict, delimiter=","):
    with open(filename, mode="w", encoding="utf-8") as file:
        for rec in data.values():
            file.write(",".join(rec.values()))
            file.write(f"\n")


# Запись в текстовый файл последнего ID словаря. Вход: словарь
def export_ID_to_file(filename: str, data: dict, delimiter=","):
    with open(filename, mode="w", encoding="utf-8") as file:
        one, two = data.popitem()
        file.write(str(one))


# Дозапись в текстовый файл. Вход:список
def rewrite_to_file(filename: str, data: list, delimiter=","):
    with open(filename, mode="a", encoding="utf-8") as file:
        for rec in data:
            file.write("".join(rec))
            file.write(f"\n")


# Чтение из текстового файла. Вход:строка. Выход:список
def import_from_file(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as data:
        a = data.read().split()
    return a

# print(import_from_file("list_of_students.csv")) ['Иванов,Иван,1В', 'Петров,Петр,4К', 'Сергеев,Серж,5Е']
# Функция cоздания записи (Фамилия, Имя, Класс) в виде словаря
def create_record(last_name: str, first_name: str, clas: str) -> dict:
    dictionary = {'last_name': last_name, 'first_name': first_name, 'class': clas}
    return dictionary

#Функция получения списка словарей, являющимися значениями для ключей (ID), для создания в дальнейшем
# словаря словарей, импортированного из файла
def create_rec(data:list) -> list:
    num_lst =[]
    for i in range(0, len(data), 3):
        num_lst.append(create_record(data[i], data[i+1], data[i+2]))
    return num_lst

# Функция импорта из словаря записи по ID и вывода в консоль с помощью textable
def import_rec_from_dic_with_ID(db: dict, rec_ID: int) -> dict:
    for key in db.keys():
        if key == rec_ID:
            rendering_dic_ID(db[rec_ID])


# Обновление имеющейся записи словаря на новую (Фамилия, Имя, Класс)
def update_record(db: dict, new_data: dict, rec_ID: int):
    db[rec_ID] = new_data
    return db


# Удаление имеющейся записи словаря по ID (Фамилия, Имя, Класс)
def delete_record(db: dict, rec_ID: int):
    db.pop(rec_ID)
    return db


# dictionary = {1: {'last_name': 'Иванов', 'first_name': 'Иван', 'class': '1А'},
#                2: {'last_name': 'Петров', 'first_name': 'Сергей', 'class': '1Б'},
#                3: {'last_name': 'Сидоров', 'first_name': 'Сидор', 'class': '1В'} }

def rendering_list(dic: dict):  # Функция рисование таблицы со всеми записями, экспортируемыми в файл/импортируемыми из файла
    table = Texttable()
    maps = [["Фамилия", "Имя", "Класс"]]
    for rec in list(dic.values()):
        val = ",".join(rec.values()).split(",")
        maps.append(val)
    table.add_rows(maps)
    print(table.draw())
# rendering_list(dictionary)

def rendering_dic_ID(dic: dict):  # Функция рисование таблицы с конкретной записью (по ID)
    # на экране консоли с помощью textable
    table = Texttable()
    value_lst = list(dic.values())
    maps = [["last_name", "first_name", "clas"], value_lst[:3]]
    table.add_rows(maps)
    print(table.draw())


def import_from_csv_without_ID(filename: str) -> list:  # Функция импорта из csv файла (без ID)
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data
# print(import_from_csv_without_ID("list_of_students.csv"))

# value_list = [['Иванов', 'Иван', '1В'], ['Петров', 'Петр', '4К'], ['Сергеев', 'Серж', '5Е']]
value_list = import_from_csv_without_ID("list_of_students.csv")
def parsing_lst_lst(val: list) -> list:  # Парсинг списка списков из csv файла (без ID) в список строк
    values = ",".join(",".join(v) for v in val)
    val_lst = values.split(",")
    return val_lst
#print(parsing_lst_lst(value_list))
val = parsing_lst_lst(value_list)
print(create_rec(val))
def import_from_file(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
    #with open("list_of_students.csv", "r") as f:
        reader = csv.reader(f, delimiter="\t")
        for i, line in enumerate(reader):
            print('line[{}] = {}'.format(i, line))
            return i, line

#добавляем запись в импортированный словарь
def add_records_in_import_dic(db: dict, rec_ID:int, data:list, mapping: dict) -> dict:
        db[rec_ID] = {name:value for name, value in zip(mapping.keys(),data)}
        return db

# data = import_from_csv_without_ID("list_of_students.csv")
# dictionary = {'last_name': "last_name", 'first_name': "first_name", 'class': "clas"}
# print(add_records_in_dic(data, dictionary))
def create_dic_from_import_csv_file(data:list) -> dict:
    db ={}
    length_dic_keys = int(len(data)/3)
    # for key in range(1, length_dic_keys + 1):
        # last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
        #for key in range(0, len(data), 3):

            #db[key] = create_record(last_name, first_name, clas)



        # for key in range(0, len(data), 3):
        #     db[key] = create_record(data[key], data[key+1], data[key+2])

    for key in range(1, length_dic_keys + 1):
        db[key] = {name: value for name, value in zip(mapping.keys(), data)}
    # for key in range(1, length_dic_keys + 1):
    # for key in range(1, length_dic_keys + 1):
    #     db[key] = create_record(data[key-1], data[key], data[key+1])
        mapping.keys()
    rendering_list(db)
    return db
# mapping = {'last_name': "last_name", 'first_name': "first_name", 'class': "clas"}
# dictionary = {'last_name': "last_name", 'first_name': "first_name", 'class': "clas"}
# print(create_dic_from_import_csv_file(val))

#for key in range(1, length_dic_keys + 1):
    #db[key] = {name: value for name, value in zip(mapping.keys(), data[key:3])}

