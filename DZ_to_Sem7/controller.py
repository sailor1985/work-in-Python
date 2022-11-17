import model, view

#1.Определяем количество записей
quantity_records = view.quantity_records()

#2. Функция заполнения структуры хранения данных (словарь)
def add_records_in_dic(quantity_records: int) -> list:
    dictionary = {}
    for key in range(1, quantity_records + 1):
        value_tup = view.add_record_surname(), view.add_record_name(), view.add_record_telephon(), view.add_record_description()
        dictionary[key] = model.create_record(value_tup)
        print("\n")
    return list(dictionary.values())

#3. Печатаем получившийся список записей
view.view_data(add_records_in_dic(quantity_records))


# model.write_to_file(value_str, "telephone directory.txt")


# def add_records_in_structure():
#     # Определяем сколько будет записей и вызываем функцию заполнения ими
#     # структуры хранения данных (словарь)
#     structure = model.struct_dic(view.quantity_records())
#     return list(structure.values())

# print(add_records_in_structure())


# lst = add_records_in_structure()
# lst = ['1, 2, 3, 4', '5, 6, 7, 8']
# view.view_data(str(lst))
# view.view_data(type(str(lst)))
# model.write_to_file("Hello world", "telephone directory.txt")
