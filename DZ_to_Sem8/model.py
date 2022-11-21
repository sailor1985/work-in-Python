from texttable import Texttable


# Запись в текстовый файл. Вход:список
def export_to_file(filename: str, data: list, delimiter=","):
    with open(filename, mode="w", encoding="utf-8") as file:
        for rec in data:
            file.write("".join(rec))
            file.write(f"\n")


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


# Создание записи (Фамилия, Имя, Класс) в виде словаря
def create_record(last_name: str, first_name: str, clas: str) -> dict:
    dictionary = {'last_name': last_name, 'first_name': first_name, 'class': clas}
    return dictionary

def add_records_in_dic(quantity_records: int, last_name: str, first_name: str, clas: str) -> dict:
    structure = {}
    for key in range(1, quantity_records + 1):
        structure[key] = create_record(last_name, first_name, clas)
        print("\n")
    return structure


# Функция импорта из словаря записи по ID и вывода в консоль
def import_rec_from_dic_with_ID(db: dict, rec_ID: int) -> dict:
    for key in db.keys():
        if key == rec_ID:
            val = db[rec_ID]
            rendering_dic_ID(val)
            break
    return val


# Обновление имеющейся записи словаря на новую (Фамилия, Имя, Класс)
def update_record(db: dict, new_data: dict, rec_ID: int):
    db[rec_ID] = new_data
    return db


# Удаление имеющейся записи словаря по ID (Фамилия, Имя, Класс)
def delete_record(db: dict, rec_ID: int):
    db.pop(rec_ID)
    return db


def parsing_lst(value_lst: list) -> str:  # Парсинг списка записей в строку
    value_str = "\n".join(value_lst)
    return value_str


def parsing_lst_for_table(value_lst: list) -> str:  # Парсинг списка записей для таблицы Textable
    value_str = ",".join(value_lst)
    return value_str


def rendering_list(dic: dict):  # Функция рисование таблицы со всеми записями, экспорт  ируемыми в файл/импортируемыми из файла
    table = Texttable()
    value_lst = list(dic.values())
    maps = [["Фамилия", "Имя", "Класс"]]
    for i in range(0, len(value_lst) - 1, 3):
        maps.append([value_lst[i], value_lst[i + 1], value_lst[i + 2]])
    table.add_rows(maps)
    print(table.draw())


def rendering_dic_ID(dic: dict):  # Функция рисование таблицы с конкретной записью (по ID)
    # на экране консоли с помощью textable
    table = Texttable()
    value_lst = list(dic.values())
    maps = [["last_name", "first_name", "clas"], value_lst[:3]]
    table.add_rows(maps)
    print(table.draw())
