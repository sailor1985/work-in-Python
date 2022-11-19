import controller as c

# Для вызова той или иной функции комментируем те, которые не нужны

# 1. Вызов функции экспорта записей в файл и их вывода на экран с помощью Textable
c.add_records_in_file_print_with_textable()

# 2. Вызов функции импорта записей из файла и их вывода на экран с помощью Textable
c.take_records_from_file_with_textable()

# 3. Вызов функции добавления записей в файл с уже имеющимися записями и вывод на экран всех записей с учетом добавленных с помощью Textable
c.add_records_in_file_with_available_records_with_textable()
