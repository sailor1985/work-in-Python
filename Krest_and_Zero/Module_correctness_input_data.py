from Module_rendering_function_with_Texttable import step_maps

def valid_input(current_gamer, maps, value):
    valid = False
    while not valid:
        step = input(f"{current_gamer.capitalize()}, выберите ячейку, в которую хотите поставить ваш знак: ")
        try:
            step = int(step)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?") 
            continue
        if step >= 1 and step <= 9:
            if (str(maps[step-1]) not in "x0"):
                step_maps(maps,step,value) # Функция заполнения списка крестиком или ноликом,
                                            # в зависимости от того что в нее передали.
                valid = True
            else:
                print("Эта клеточка уже занята")
                continue
        else:
                print("Некорректный ввод. Введите число от 1 до 9 чтобы сделать ход.")
                continue
        