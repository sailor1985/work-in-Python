def read_data(filename: str) -> list:  #Чтение из текстового файла. Вход:строка. Выход:список
    with open(filename, "r", encoding = "utf-8") as data:
        a = data.read().split(", ")
    return a