# 1. Напишите программу, удаляющую из текста все слова, содержащие "abc".
# Примечание Текст находится в файле. Его надо считать, текст исправить,
# исправленный текст записать в новый файл.
# Использовать вложенный менеджер контекста

import Module2_read_from_txt_file as M2, Module3_del_find_element_in_str as M3
import Module1_write_in_txt_file as M1

# 1. Считываем текст из файла test5.txt. На выходе строка.
text = ', '.join(M2.read_data("test5.txt")) 
print(text)

#2. Вызываем функцию, удаляющая из текста все слова, содержащие "abc"
find_el = "abc"
text_new = M3.del_find_elem_from_str(find_el, text)
print(text_new)

#3. Запись исправленного текста в новый файл.
M1.write_to_file(text_new, "test6.txt")