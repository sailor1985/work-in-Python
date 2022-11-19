from texttable import Texttable


def export_to_file(filename: str, data: list, delimiter=","):  # Запись в текстовый файл. Вход:список
    with open(filename, mode="w", encoding="utf-8") as file:
        for rec in data:
            file.write("".join(rec))
            file.write(f"\n")


def rewrite_to_file(filename: str, data: list, delimiter=","):  # Дозапись в текстовый файл. Вход:список
    with open(filename, mode="a", encoding="utf-8") as file:
        for rec in data:
            file.write("".join(rec))
            file.write(f"\n")


def import_from_file(filename: str) -> list:  # Чтение из текстового файла. Вход:строка. Выход:список
    with open(filename, "r", encoding="utf-8") as data:
        a = data.read().split()
    return a


def create_record(value_tup: tuple) -> str:  # Добавление записи (Фамилия, Имя, Телефон, Описание)
                                             # в строковую переменную
    value_str = ",".join(value_tup)
    return value_str


def parsing_lst(value_lst: list) -> str:  # Парсинг списка записей в строку
    value_str = "\n".join(value_lst)
    return value_str


def parsing_lst_for_table(value_lst: list) -> str:  # Парсинг списка записей для таблицы
    value_str = ",".join(value_lst)
    return value_str


def rendering_list(value_lst: list):  # Функция рисование таблицы со всеми записями, экспортируемыми в файл/импортируемыми из файла
    table = Texttable()
    maps = [["Фамилия", "Имя", "Телефон", "Описание"]]
    for i in range(0, len(value_lst), 4):
        maps.append([value_lst[i], value_lst[i + 1], value_lst[i + 2], value_lst[i + 3]])
    table.add_rows(maps)
    print(table.draw())
