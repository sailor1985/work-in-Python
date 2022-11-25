import controller as c

# Для вызова той или иной функции комментируем те, которые не нужны

# 1. CREATE
# c.export_add_records_of_dic_to_csv_file()

# На следующей строчке результат - CREATE: словарь dictionary. Раскомментировать строчки 9-11 для использования в READ,UPDATE,DELETE
# dictionary = {1: {'last_name': 'Иванов', 'first_name': 'Иван', 'class': '1А'},
#                2: {'last_name': 'Петров', 'first_name': 'Сергей', 'class': '1Б'},
#                3: {'last_name': 'Сидоров', 'first_name': 'Сидор', 'class': '1В'} }

# 2. READ
# c.import_ID(dictionary)

# 3. UPDATE
# c.update_rec_ID(dictionary)

# 4. DELETE
# c.delete_rec_ID(dictionary)

# 5. Импорт из CSV файла без ID и наполнение БД
# c.import_from_csv_file_without_ID()

# 6. Добавление записи (Фамилия, Имя, Класс) в импортированный словарь по ID
#c.add_rec_ID_to_dic(c.import_from_csv_file_without_ID())