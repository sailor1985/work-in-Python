def write_to_file(string, filename):  #Запись в текстовый файл. Вход:строка
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(string)