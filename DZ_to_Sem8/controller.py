import model, view
import csv


# 1. CREATE: Создаем запись по заданному множеству полей и записываем ее в БД. Поля вводятся пользователем.

def add_records_in_dic() -> dict:
    quantity_records = view.quantity_records()
    structure = {}
    for key in range(1, quantity_records + 1):
        last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
        structure[key] = model.create_record(last_name, first_name, clas)
        print("\n")
    return view.view_data(structure)

# На следующей строчке результат - CREATE: словарь dictionary. Раскомментировать строчку 17 для использования в READ,UPDATE,DELETE
dictionary = {1: {'last_name': 'Гончаров', 'first_name': 'Михаил', 'class': '11А'},
              2: {'last_name': 'Петров', 'first_name': 'Сергей', 'class': '3В'}}

# 2. WRITE: Экспорт в данных в csv файл и последнего ID словаря в файл Id.txt
def export_to_csv_file():
    model.export_to_file("list_of_students.csv", dictionary, delimiter=",")
    model.export_ID_to_file("Id.txt", dictionary, delimiter=",")


# 3. READ: Извлечение записи по ID из словаря и вывод в консоль с помощью textable
def import_ID():
    rec_ID = view.input_ID()
    model.import_rec_from_dic_with_ID(dictionary, rec_ID)
    if not rec_ID in dictionary:
        view.view_ID()

# 4. UPDATE: Обновление записи по ID и вывод в консоль с помощью textable обновленного словаря
def update_rec_ID():
    last_name, first_name, clas = view.add_record_surname(), view.add_record_name(), view.add_record_class()
    new_record = model.create_record(last_name, first_name, clas)
    rec_ID = view.input_ID()
    if rec_ID in dictionary:
        dic = model.update_record(dictionary, new_record, rec_ID)
        model.rendering_list(dic)
    else: view.view_ID()

# 5. DELETE: Удалить запись по ID
def delete_rec_ID():
    rec_ID = view.input_ID()
    if rec_ID in dictionary:
         dic = model.delete_record(dictionary, rec_ID)
         model.rendering_list(dic)
    else: view.view_ID()

# 6. Импорт из CSV файла с ID. Использовать пакет csv стандартной библиотеки.
# Пример:
# 1#Сидоров#Алексей#9А
# 2#Соколов#Григорий#9А
# Данные в БД добавляются, считаем, что уникальность реализуется с помощью ID.

# 7. Импорт из CSV файла без ID
def import_from_csv_file():
    model.import_from_csv_without_ID("list_of_students.csv")
