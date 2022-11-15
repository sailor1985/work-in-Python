import view

def write_to_file(string, filename):  #Запись в текстовый файл. Вход:строка
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(string)

def read_data(filename: str) -> list:  #Чтение из текстового файла. Вход:строка. Выход:список
    with open(filename, "r", encoding = "utf-8") as data:
        a = data.read().split(", ")
    return a

def add_value(): # Добавление записи (Фамилия, Имя, Телефон, Описание)
    value_tup = view.add_record_surname(), view.add_record_name(), view.add_record_telephon(), view.add_record_description()
    value_str = ", ".join(value_tup)
    return value_str

def struct_dic(quantity_records: int) -> dict: # Структура хранения данных (словарь)
    dictionary = {}
    for key in range(1, quantity_records+1):
        dictionary[key] = add_value()
        print("\n")
    return dictionary