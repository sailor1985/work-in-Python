import model, view

#1.Определяем количество записей
quantity_records = view.quantity_records()

#2. Функция заполнения записями структуры хранения данных (словарь). Возвращаем список строк со значениями словаря
def add_records_in_dic(quantity_records: int) -> list:
    dictionary = {}
    for key in range(1, quantity_records + 1):
        value_tup = view.add_record_surname(), view.add_record_name(), view.add_record_telephon(), view.add_record_description()
        dictionary[key] = model.create_record(value_tup)
        print("\n")
    return list(dictionary.values())

#3. Печатаем получившийся список со строковыми записями
# view.view_data(add_records_in_dic(quantity_records))

#4. Записываем в файл записи
model.write_to_file("telephone directory.txt", add_records_in_dic(quantity_records), delimiter=",")
