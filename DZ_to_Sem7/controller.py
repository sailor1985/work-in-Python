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
    records = add_records_in_dic()
    model.export_to_file("telephone directory.txt", records, delimiter=",")
    print("В файл записаны следующие записи:")
    records_str = model.parsing_lst(records)
    view.view_data(records_str)


#4. Считываем из файла записи
#a = model.import_from_file("telephone directory.txt")
#view.view_data(a)

#5. Добавление записей в файл с уже имеющимися записями
#model.rewrite_to_file("telephone directory.txt", add_records_in_dic(), delimiter=",")