import model, view
import csv

# 1. CREATE: Функция заполнения записями структуры хранения данных (словарь)
def add_records_in_dic() -> dict:
    quantity_records = view.quantity_records()
    structure = {}
    for key in range(1, quantity_records + 1):
        last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
        structure[key] = model.create_record(last_name, first_name, clas)
        print("\n")
    return structure

# dic_all = add_records_in_dic(quantity_records)
# view.view_data(dic_all)
dictionary = {1: {'last_name': 'Гончаров', 'first_name': 'Михаил', 'class': '11А'}, 2: {'last_name': 'Петров', 'first_name': 'Сергей', 'class': '3В'}}

#2. READ: Функция импорта из структуры хранения данных (словарь) записи по ID и вывода в консоль
# с помощью textable
def import_rec_from_dic_with_ID(db: dict) -> dict:
    rec_ID = view.input_ID()
    for key in db.keys():
        if key == rec_ID:
            val = db[rec_ID]
            model.rendering_dic_ID(val)
            break 
    return val

# import_rec_from_dic_with_ID(dic_all)

#3. UPDATE: Обновить запись по ID
def new_record_to_dic():
    last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
    dictionary = model.create_record(last_name, first_name, clas)
    return dictionary

new_record = new_record_to_dic()
view.view_data(new_record)
rec_ID = view.input_ID()

def update_record(db:dict, new_data: dict, rec_ID: int):
    db[rec_ID] = new_data
    return db

update_value = update_record(dictionary, new_record, rec_ID)
view.view_data(update_value)