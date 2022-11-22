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


# Функция cоздания записи (Фамилия, Имя, Класс) в виде словаря
def create_record(last_name: str, first_name: str, clas: str) -> dict:
    dictionary = {'last_name': last_name, 'first_name': first_name, 'class': clas}
    return dictionary


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


def rendering_list(dic: dict):  # Функция рисование таблицы со всеми записями, экспортируемыми в файл/импортируемыми из файла
    table = Texttable()
    maps = [["Фамилия", "Имя", "Класс"]]
    for rec in list(dic.values()):
        val = ",".join(rec.values()).split(",")
        maps.append(val)
    table.add_rows(maps)
    print(table.draw())


def rendering_dic_ID(dic: dict):  # Функция рисование таблицы с конкретной записью (по ID)
    # на экране консоли с помощью textable
    table = Texttable()
    value_lst = list(dic.values())
    maps = [["last_name", "first_name", "clas"], value_lst[:3]]
    table.add_rows(maps)
    print(table.draw())


def import_from_csv_without_ID(filename: str):  # Функция импорта из csv файла (без ID)
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))


def import_from_csv_with_ID(filename: str):  # Функция импорта из csv файла (c ID)
    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for row in reader:
            print(','.join(row))
