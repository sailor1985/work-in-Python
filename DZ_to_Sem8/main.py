import  controller as c

# Для вызова той или иной функции комментируем те, которые не нужны

# 1. CREATE
#c.add_records_in_dic()

# На следующей строчке результат - CREATE: словарь dictionary. Раскомментировать строчки 9-10 для использования в READ,UPDATE,DELETE
# dictionary = {1: {'last_name': 'Иванов', 'first_name': 'Иван', 'class': '1А'},
#                2: {'last_name': 'Петров', 'first_name': 'Сергей', 'class': '1Б'},
#                3: {'last_name': 'Сидоров', 'first_name': 'Сидор', 'class': '1В'} }

# 2. WRITE
#c.export_to_csv_file()

# 3. READ
# c.import_ID(dictionary)

#4. UPDATE
# c.update_rec_ID(dictionary)

#5. DELETE
# c.delete_rec_ID(dictionary)

# 7. Импорт из CSV файла без ID
#c.import_from_csv_file()