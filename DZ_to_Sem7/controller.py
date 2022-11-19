import model, view

#1.Определяем количество записей
quantity_records = view.quantity_records()

#2. Функция заполнения записями структуры хранения данных (словарь). Возвращаем список строк со значениями словаря
def add_records_in_dic(quantity_records: int) -> list:
    dictionary = {}
    for key in range(1, quantity_records + 1):
        record_tup = view.add_record_surname(), view.add_record_name(), view.add_record_telephon(), view.add_record_description()
        dictionary[key] = model.create_record(record_tup)
        print("\n")
    return list(dictionary.values())

#3. Записываем в файл записи
# model.export_to_file("telephone directory.txt", add_records_in_dic(quantity_records), delimiter=",")

#4. Считываем из файла записи
#a = model.import_from_file("telephone directory.txt")
#view.view_data(a)

#5. Добавление записей в файл с уже имеющимися записями
model.rewrite_to_file("telephone directory.txt", add_records_in_dic(quantity_records), delimiter=",")