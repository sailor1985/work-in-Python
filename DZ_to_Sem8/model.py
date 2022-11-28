from texttable import Texttable
import csv


# Словарь для хардкорной проверки
# dictionary = {1:{'last_name': 'Иванов', 'first_name': 'Иван', 'class': '1А'},
# 2:{'last_name': 'Петров', 'first_name': 'Сергей', 'class': '1Б'},
# 3:{'last_name': 'Сидоров', 'first_name': 'Сидор', 'class': '1В'}}


# Функция конвертации импортированного слвоаря словарей в список для последующей записи в csv файл (с ID)
def convert_lst(dict: dict) -> list:
    id_dict = {}
    id_list = []
    for i in range(1, len(dict) + 1):
        id_dict[str(i)] = ({'ID': str(i)})
        id_dict[str(i)].update(dict[i])
        id_list.append(id_dict.setdefault(str(i)))
    return id_list


# Функция экспорта в csv файл (с ID)
def export_to_file_csv_with_ID(dict_group: dict):
    num_list = convert_lst(dict_group)
    with open('Students_with_ID.csv', mode='w', encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(num_list[0].keys()), quoting=csv.QUOTE_NONNUMERIC, lineterminator="\r")
        writer.writeheader()
        for d in num_list:
            writer.writerow(d)


# Запись в текстовый файл последнего ID словаря. Вход: словарь
def export_ID_to_file(filename: str, data: dict):
    with open(filename, mode="w", encoding="utf-8") as file:
        one, two = data.popitem()
        file.write(str(one))


# Чтение из текстового файла последнего ID словаря. Вход:строка. Выход:число
def import_ID_from_file(filename: str) -> int:
    with open(filename, "r", encoding="utf-8") as data:
        a = int(data.read())
    return a


# Функция cоздания записи (Фамилия, Имя, Класс) в виде словаря
def create_record(last_name: str, first_name: str, clas: str) -> dict:
    dictionary = {'last_name': last_name, 'first_name': first_name, 'class': clas}
    return dictionary


# Функция получения списка словарей, являющимися значениями для ключей (ID), для создания в дальнейшем
# словаря словарей, импортированного из файла
def values_from_import_csv_file_to_create_dic(data: list) -> list:
    num_lst = []
    for i in range(0, len(data) - 1, 3):
        num_lst.append(create_record(data[i], data[i + 1], data[i + 2]))
    return num_lst


# Функция импорта из словаря записи по ID и вывода в консоль с помощью textable
def import_rec_from_dic_with_ID(db: dict, rec_ID: int) -> dict:
    for key in db.keys():
        if key == rec_ID:
            rendering_dic_ID(db[rec_ID])


# Добавление записи (Фамилия, Имя, Класс) в словарь по ID
def add_record(db: dict, new_data: dict, rec_ID: int):
    db[rec_ID] = new_data
    return db


# Удаление имеющейся записи словаря (Фамилия, Имя, Класс) по ID
def delete_record(db: dict, rec_ID: int):
    db.pop(rec_ID)
    return db


# Функция рисования таблицы со всеми записями, экспортируемыми в файл/импортируемыми из файла csv без ID
def rendering_list(dic: dict):
    table = Texttable()
    maps = [["Фамилия", "Имя", "Класс"]]
    for rec in list(dic.values()):
        val = ",".join(rec.values()).split(",")
        maps.append(val)
    table.add_rows(maps)
    print(table.draw())


# Функция рисования таблицы со всеми записями, экспортируемыми в файл/импортируемыми из файла csv c ID
def rendering_list_with_ID(value_lst: list):
    table = Texttable()
    maps = [["ID", "Фамилия", "Имя", "Класс"]]
    for i in range(0, len(value_lst) - 1, 4):
        maps.append([value_lst[i], value_lst[i + 1], value_lst[i + 2], value_lst[i + 3]])
    table.add_rows(maps)
    print(table.draw())


# Функция рисование таблицы с конкретной записью (по ID) на экране консоли с помощью textable
def rendering_dic_ID(dic: dict):
    table = Texttable()
    value_lst = list(dic.values())
    maps = [["last_name", "first_name", "clas"], value_lst[:3]]
    table.add_rows(maps)
    print(table.draw())


# Функция импорта из csv файла (без ID)
def import_from_csv_without_ID(filename: str) -> list:
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        data = list(reader)
    return data


# Парсинг списка списков из csv файла (без ID) в список строк
def parsing_lst_lst(val: list) -> list:
    values = ",".join(",".join(v) for v in val)
    val_lst = values.split(",")
    return val_lst


# Функция заполнения БД (словаря словарей) записями с присвоением ID (ключей) из импортированного файла csv без ID
def create_dic_from_import_csv_file(data: list) -> dict:
    db = {}
    for i, dic in enumerate(data, 1):
        db[i] = dic
    rendering_list(db)
    return db
