import model, view

#1. Функция заполнения записями структуры хранения данных (словарь). Возвращает список строк со значениями словаря
def add_records_in_dic() -> list:
    quantity_records = view.quantity_records() #Определяем количество записей
    dictionary = {}
    for key in range(1, quantity_records + 1):
        record_tup = view.add_record_surname(), view.add_record_name(), view.add_record_telephon(), view.add_record_description()
        dictionary[key] = model.create_record(record_tup)
        print("\n")
    return list(dictionary.values())


#2. Функция экспорта записей в файл и их вывода на экран
def add_records_in_file():
    records_lst = add_records_in_dic()
    model.export_to_file("telephone directory.txt", records_lst, delimiter=",")
    print("В файл записаны следующие записи:")
    records_str = model.parsing_lst(records_lst)
    view.view_data(records_str)

#3. Функция импорта записей из файла и их вывода на экран
def take_records_from_file():
    records_lst = model.import_from_file("telephone directory.txt")
    records_str = model.parsing_lst(records_lst)
    print("Из файла cчитаны следующие записи:")
    view.view_data(records_str)

#4. Функция добавления записей в файл с уже имеющимися записями и вывода на экран всех записей с учетом добавленных
def add_records_in_file_with_available_records():
    records_lst = add_records_in_dic()
    model.rewrite_to_file("telephone directory.txt", records_lst, delimiter=",")
    print("В файл дозаписаны следующие записи:")
    records_str = model.parsing_lst(records_lst)
    view.view_data(records_str)

def add_records_in_file_print_with_textable() -> list:
    records_lst = add_records_in_dic()
    model.export_to_file("telephone directory.txt", records_lst, delimiter=",")
    print("В файл записаны следующие записи:")
    records_str = model.parsing_lst_for_table(records_lst)
    records = records_str.split(",")
    view.view_data(records)
    view.view_data(type(records))

add_records_in_file_print_with_textable()

# ['Иванов,Иван,123,Бос', 'Петров,Петр,234,Инженер']
#records_str = model.parsing_lst(records_lst)