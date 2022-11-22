import  controller as c

# 1. CREATE
#c.add_records_in_dic()

# На следующей строчке результат - CREATE: словарь dictionary. Раскомментировать строчку 7 для использования в READ,UPDATE,DELETE
dictionary = {1: {'last_name': 'Гончаров', 'first_name': 'Михаил', 'class': '11А'},
              2: {'last_name': 'Петров', 'first_name': 'Сергей', 'class': '3В'}}

# 2. WRITE
# c.export_to_csv_file()

# 3. READ
# c.import_ID()

#4. UPDATE
# c.update_rec_ID()

#5. DELETE
# c.delete_rec_ID()

# 7. Импорт из CSV файла без ID
c.import_from_csv_file()