import model, view

def storage_structure():
    q = view.quantity_records() # Определяем сколько будет записей
    structure = model.struct_dic(q) # Вызываем структуру хранения данных (словарь), заполненный записями
    print(structure)

storage_structure()

    # value_a = view.add_record()
    # value_b = view.add_record()

    # model.init(value_a, value_b)
    # result = model.sum()
    # view.view_data(result)

