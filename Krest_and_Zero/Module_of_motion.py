from random import choice
from Module_data_structure import struct_list
from Module_rendering_function_with_Texttable import rendering_list, step_maps

def tic_tac_toe_with_2_players(): #Функция игры 2 игроков
    gamer_1, gamer_2 = input("Введите имя 1 игрока (рисует x): "), input("Введите имя 2 игрока (рисует 0): ")
    player_lst = [gamer_1, gamer_2]
    current_gamer = choice(player_lst)
    print("\nСейчас начнется жеребьевка за право первого хода!\n\n"
     f"Поздравляем, {current_gamer.capitalize()}, право первого хода предоставлено тебе!\n")

    number_of_remaining_cells = 9
    print("Текущее состояние поля клеток:")
    rendering_list(struct_list())

    while number_of_remaining_cells:
        while True:
            if current_gamer == gamer_1:
                value = "x"
                step = int(input(f"{current_gamer.capitalize()}, ваш ход: "))
            else:
                value = "0"
                current_gamer = gamer_2
                step = int(input(f"{current_gamer.capitalize()}, ваш ход: "))

            rendering_list(step_maps(struct_list(),step,value))

            #Проверка коорректности ввода номера ячейки
            if step == "":
                print("\nПустой ввод. Повторите снова:" ) 
                continue
            else:
                break
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1

tic_tac_toe_with_2_players()