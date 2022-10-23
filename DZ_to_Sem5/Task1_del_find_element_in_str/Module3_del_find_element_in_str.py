def del_find_elem_from_str(find_str, text_str ): #Нахождение и удаление искомого элемента из строки
    text_str = text_str.replace(find_str, "") # Удалили заданные символы из строки
    text_lst = text_str.split(", ") # Разделили полученную строку по заданным символам и получили список
    text_lst = list(filter(None, text_lst)) #Отфильтовали пустые элементы списка
    text = ', '.join(text_lst) # Итоговая строка с учетом удаления из нее заданных символов
    return text 