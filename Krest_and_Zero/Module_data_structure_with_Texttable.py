def structure_text():
    from texttable import Texttable
    from random import sample

    el1 = sample(["X", "0", ""], k =3)
    el2 = sample(["X", "0", ""], k =3)
    el3 = sample(["X", "0", ""], k =3)

    table = Texttable()  
    table.add_rows([["1", "2", "3"], el1, el2, el3])
    print(table.draw())