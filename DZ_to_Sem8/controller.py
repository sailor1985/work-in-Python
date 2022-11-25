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


# 2. WRITE: Экспорт словаря с созданными записями в csv файл и последнего  его ID в файл Id.txt
def export_add_records_of_dic_to_csv_file():
    dictionary = add_records_in_dic()
    model.export_to_file("list_of_students.csv", dictionary, delimiter=",")
    model.export_ID_to_file("Id.txt", dictionary, delimiter=",")


# 3. READ: Извлечение записи по ID из словаря и вывод в консоль с помощью textable
def import_ID(dictionary):
    rec_ID = view.input_ID()
    model.import_rec_from_dic_with_ID(dictionary, rec_ID)
    if not rec_ID in dictionary:
        view.view_ID()


# 4. UPDATE: Обновление записи по ID и вывод в консоль с помощью textable обновленного словаря
def update_rec_ID(dictionary):
    last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
    new_record = model.create_record(last_name, first_name, clas)
    rec_ID = view.input_ID()
    if rec_ID in dictionary:
        dic = model.update_record(dictionary, new_record, rec_ID)
        model.rendering_list(dic)
    else:
        view.view_ID()


# 5. DELETE: Удалить запись по ID
def delete_rec_ID(dictionary):
    rec_ID = view.input_ID()
    if rec_ID in dictionary:
        dic = model.delete_record(dictionary, rec_ID)
        model.rendering_list(dic)
    else:
        view.view_ID()


# 6. Импорт из CSV файла с ID. Использовать пакет csv стандартной библиотеки.
# Пример:
# 1#Сидоров#Алексей#9А
# 2#Соколов#Григорий#9А
# Данные в БД добавляются, считаем, что уникальность реализуется с помощью ID.
# add_records_in_dic(db: dict, rec_ID:int, data:list, mapping: dict)

# 7. Импорт из CSV файла без ID


