from texttable import Texttable

def rendering(dictinary: dict): #Функция рисование поля клеток с отображением
                                #текущего состояния (frontend в консоли)
    lst = list(dictinary.values()) #Вытащили из словаря все значения в список
    table = Texttable() 
    table.add_rows([["1", "2", "3"], lst[:3], lst[3:6], lst[6:9]])
    print(table.draw())