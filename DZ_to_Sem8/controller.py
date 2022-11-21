import model, view
import csv

# 1. CREATE: Функция заполнения записями структуры хранения данных (словарь)
#quantity_records = view.quantity_records()
def add_records_in_dic(quantity_records: int) -> dict:
    structure = {}
    for key in range(1, quantity_records + 1):
        last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
        structure[key] = model.create_record(last_name, first_name, clas)
        print("\n")
    return structure

#dictionary = add_records_in_dic(quantity_records)
#view.view_data(dictionary)

# 2. WRITE: Экспорт в csv файл
#model.export_to_file("list_of_students.csv", dictionary, delimiter=",")

# На следующей строчке результат - CREATE: словарь dictionary для использования в READ,UPDATE,DELETE
# dictionary = {1: {'last_name': 'Гончаров', 'first_name': 'Михаил', 'class': '11А'}, 2: {'last_name': 'Петров', 'first_name': 'Сергей', 'class': '3В'}}

# 4. READ: Функция импорта из структуры хранения данных (словарь) записи по ID и вывода в консоль
# с помощью textable
# rec_ID = view.input_ID()
# model.import_rec_from_dic_with_ID(dictionary, rec_ID)

# 5. UPDATE: Обновить запись по ID
#last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
#new_record = model.create_record(last_name, first_name, clas)
#rec_ID = view.input_ID()
#if rec_ID in dictionary:
    #view.view_data(model.update_record(dictionary, new_record, rec_ID))
#else: view.view_ID()

# 6. DELETE: Удалить запись по ID
# rec_ID = view.input_ID()
# if rec_ID in dictionary:
#     view.view_data(model.delete_record(dictionary, rec_ID))
# else: view.view_ID()

# 5. WRITE: Экспорт в csv файл
def add_records_in_file_print_with_textable():
    records_lst = add_records_in_dic()
    model.export_to_file("list_of_students.csv", dictionary, delimiter=",")
    view.view_data("В файл записаны следующие записи:")
    records_str = model.parsing_lst_for_table(records_lst)
    records = records_str.split(",")
    model.rendering_list(records)
    return records_lst

model.export_to_file("list_of_students.csv", dictionary, delimiter=",")



#5. - Импорт из CSV файла с ID. Использовать пакет csv стандартной библиотеки.
# Пример:
# 1#Сидоров#Алексей#9А
# 2#Соколов#Григорий#9А
# Данные в БД добавляются, считаем, что уникальность реализуется с помощью ID.

#csv.reader()

# 2. Функция экспорта записей в файл и их вывода на экран с помощью Textable
