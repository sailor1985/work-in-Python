from Module_rendering_function_with_Texttable import step_maps

# maps = list(range(1,10))
def correct_input(value, maps, step: str):
    try:
        step = int(step)
    except:
        print("Некорректный ввод. Вы уверены, что ввели число?") 
        continue
    if step >= 1 and step <= 9:
        if (str(maps[step-1]) not in "x0"):
            maps[step-1] = value
            valid = True
        else:
            print("Эта клеточка уже занята")
            continue
    else:
        print("Некорректный ввод. Введите число от 1 до 9 чтобы сделать ход.")
        continue
    
    return step