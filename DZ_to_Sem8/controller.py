import model, view


# 1. CREATE: Создаем запись по заданному множеству полей и записываем ее в БД. Поля вводятся пользователем.

def add_records_in_dic() -> dict:
    quantity_records = view.quantity_records()
    structure = {}
    for key in range(1, quantity_records + 1):
        last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
        structure[key] = model.create_record(last_name, first_name, clas)
        print("\n")
    model.rendering_list(structure)
    return structure


# 2. READ: Извлечение записи по ID из словаря и вывод в консоль с помощью textable
def import_ID(dictionary):
    rec_ID = view.input_ID()
    model.import_rec_from_dic_with_ID(dictionary, rec_ID)
    if not rec_ID in dictionary:
        view.view_ID()


# 3. UPDATE: Обновление записи по ID и вывод в консоль с помощью textable обновленного словаря
def update_rec_ID(dictionary):
    last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
    new_record = model.create_record(last_name, first_name, clas)
    rec_ID = view.input_ID()
    if rec_ID in dictionary:
        dic = model.add_record(dictionary, new_record, rec_ID)
        model.rendering_list(dic)
    else:
        view.view_ID()


# 4. DELETE: Удалить запись по ID
def delete_rec_ID(dictionary):
    rec_ID = view.input_ID()
    if rec_ID in dictionary:
        dic = model.delete_record(dictionary, rec_ID)
        model.rendering_list(dic)
    else:
        view.view_ID()


# 5. Импорт из CSV файла без ID в словарь
def import_from_csv_file_without_ID():
    value_list = model.import_from_csv_without_ID("Students_without_ID.csv")
    val = model.parsing_lst_lst(value_list)
    val_csv = model.values_from_import_csv_file_to_create_dic(val)
    db = model.create_dic_from_import_csv_file(val_csv)
    view.view_data(db)
    return db


# 6. Добавление записи (Фамилия, Имя, Класс) в импортированный словарь с присвоенем ID
def add_rec_ID_to_dic(dictionary):
    last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
    new_record = model.create_record(last_name, first_name, clas)
    rec_ID = view.input_ID()
    last_ID = model.import_ID_from_file("Id.txt")
    if rec_ID == last_ID + 1:
        dic = model.add_record(dictionary, new_record, rec_ID)
        model.rendering_list(dic)
        view.view_data(dic)
        return dic
    else:
        view.view_ID()


# 7. Экспорт полученного выше словаря в csv файл с ID и последней "ID" записи в файл Id.txt
def export_add_records_of_dic_to_csv_file_with_ID():
    db1 = import_from_csv_file_without_ID()
    add_db1 = add_rec_ID_to_dic(db1)
    model.export_to_file_csv_with_ID(add_db1)
    model.export_ID_to_file("Id.txt", add_db1)


# 8. Импорт из CSV файла с ID
def import_from_csv_file_with_ID():
    value_list = model.import_from_csv_without_ID("Students_with_ID.csv")
    value_list.pop(0)
    val_pars = model.parsing_lst_lst(value_list)
    model.rendering_list_with_ID(val_pars)
    return val_pars
