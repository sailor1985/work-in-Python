def structure_pretty(): # Структура хранения данных и ее случайное заполнение
    from prettytable import PrettyTable
    from random import sample

    el1 = sample(["X", "0", ""], k =3)
    el2 = sample(["X", "0", ""], k =3)
    el3 = sample(["X", "0", ""], k =3)

    table = PrettyTable(["1", "2", "3"])
    table.add_row(el1)
    table.add_row(el2)
    table.add_row(el3)
    print(table)