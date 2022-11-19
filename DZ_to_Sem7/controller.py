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




#5. Добавление записей в файл с уже имеющимися записями
#model.rewrite_to_file("telephone directory.txt", add_records_in_dic(), delimiter=",")