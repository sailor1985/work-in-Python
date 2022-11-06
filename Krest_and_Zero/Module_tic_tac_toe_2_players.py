from random import choice
from Module_rendering_function_with_Texttable import rendering_list, step_maps
import keyboard

def tic_tac_toe_with_2_players(number_of_cells = 9): #Функция игры 2 игроков
    gamer_1, gamer_2 = input("Введите имя 1 игрока (рисует x): "), input("Введите имя 2 игрока (рисует 0): ")
    player_lst = [gamer_1, gamer_2]
    current_gamer = choice(player_lst)
    print("\nСейчас начнется жеребьевка за право первого хода!\n\n"
     f"Поздравляем, {current_gamer.capitalize()}, право первого хода предоставлено вам!\n")
    
    maps = list(range(1,10)) #Структура хранения данных (список), заполненная цифрами в диапозоне от 1 до 9,
                             #которые являются вводимыми данным игроков для того, чтобы показать в какую ячейку
                             #поставить свой знак: x или 0

    print("Текущее состояние поля клеток")
    rendering_list(maps) # Показываем исходное состояние поля клеток,
                         # используя функцию рисования поля клеток с отображением
                         # текущего состояния
    
    while number_of_cells != 0:
        print(f"Количество оставшихся ячеек: {number_of_cells}")
        valid = False
        count = 0
        print("Чтобы прервать игру нажмите клавишу q, продолжить - пробел: ")
        if keyboard.read_key() == "q":
            print("Игра прервана игроком")
            break
        while not valid:
            if keyboard.read_key() == "q":
                print("Игра прервана игроком")
                break
            if current_gamer == gamer_1: value = "x"
            else: value = "0"
            step = input(f"{current_gamer.capitalize()}, выберите ячейку, в которую хотите поставить ваш знак: ")

            # Проверка корректности ввода номера ячейки (ввод строки, пустого значения, значения не их диапозона от 1 до 9,
            # а также проверка условия занятости ячейки
            try:
                step = int(step)
            except:
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
        rendering_list(maps)  # Показываем очередное текущее состояние поля клеток с учетом введенных ранее символов
        count += 1             
        number_of_cells -= count
        # current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1

        if current_gamer == gamer_1:
            current_gamer = gamer_2
        else: current_gamer = gamer_1
    print("Игра завершена")

tic_tac_toe_with_2_players()