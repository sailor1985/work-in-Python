import controller as c

#1. Вызов функции экспорта записей в файл и их вывода на экран
c.add_records_in_file()

#2. Вызов функции импорта записей из файла и их вывода на экран
c.take_records_from_file()

#3. Вызов функции добавления записей в файл с уже имеющимися записями
c.add_records_in_file_with_available_records()