import model, view
import csv

# 1. Функция заполнения записями структуры хранения данных (словарь)
def add_records_in_dic() -> dict:
    quantity_records = view.quantity_records()
    structure = {}
    for key in range(1, quantity_records + 1):
        last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
        structure[key] = model.create_record(last_name, first_name, clas)
        print("\n")
    return structure

# dic_all = add_records_in_dic()
# view.view_data(dic_all)
# dictionary = dic_all

#2. READ: Функция импорта из структуры хранения данных (словарь) записи по ID и вывода в консоль
# с помощью textable
def import_rec_from_dic_with_ID(dic_all: dict) -> dict:
    ID = view.input_ID()
    for key in dic_all.keys():
        if key == ID:
            val = dic_all[ID]
            model.rendering_dic_ID(val)
            break 
    return val

# import_rec_from_dic_with_ID(dictionary)


# 2. Функция экспорта записей в файл и их вывода на экран с помощью Textable
def add_records_in_file_print_with_textable():
    records_lst = add_records_in_dic()
    model.export_to_file("telephone directory.txt", records_lst, delimiter=",")
    view.view_data("В файл записаны следующие записи:")
    records_str = model.parsing_lst_for_table(records_lst)
    records = records_str.split(",")
    model.rendering_list(records)
    return records_lst


# 3. Функция импорта записей из файла и их вывода на экран с помощью Textable
def take_records_from_file_with_textable():
    records_lst = model.import_from_file("telephone directory.txt")
    view.view_data("Из файла cчитаны следующие записи:")
    records_str = model.parsing_lst_for_table(records_lst)
    records = records_str.split(",")
    model.rendering_list(records)
    return records_lst


# 4. Функция добавления записей в файл с уже имеющимися записями и вывода на экран всех записей с учетом добавленных с помощью Textable
def add_records_in_file_with_available_records_with_textable():
    records_lst = add_records_in_dic()
    model.rewrite_to_file("telephone directory.txt", records_lst, delimiter=",")
    view.view_data("В файл дозаписаны следующие записи:")
    records_str = model.parsing_lst_for_table(records_lst)
    records = records_str.split(",")
    model.rendering_list(records)
    return records_lst
