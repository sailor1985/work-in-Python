def structure(): # Структура хранения данных (словарь) и его случайное заполнение
    from random import choice

    structure_dic = dict.fromkeys(['x1y1','x1y2','x1y3','x2y1','x2y2','x2y3','x3y1','x3y2','x3y3' ], '')
    for key in structure_dic:
        structure_dic[key] = choice(["X", "0", ""])
    return structure_dic