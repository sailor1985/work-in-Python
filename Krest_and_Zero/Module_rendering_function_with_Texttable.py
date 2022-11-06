from texttable import Texttable

def rendering_random_dic(dictinary: dict): #Функция рисование поля клеток с отображением
                                           #рандомного текущего состояния (frontend в консоли)
    lst = list(dictinary.values()) #Вытащили из словаря все значения в список
    table = Texttable() 
    table.add_rows([["1", "2", "3"], lst[:3], lst[3:6], lst[6:9]])
    print(table.draw())

def rendering_list(maps: list): #Функция рисование поля клеток с отображением
                                #текущего состояния (frontend в консоли)
    table = Texttable() 
    table.add_rows([[], maps[:3], maps[3:6], maps[6:9]])
    print(table.draw())
    return maps

def step_maps(maps: list,cell_number: int,symbol: str): # Функция заполнения списка крестиком или ноликом,
                                                        # в зависимости от того что в нее передали.
    ind = maps.index(cell_number)
    maps[ind] = symbol
    return maps