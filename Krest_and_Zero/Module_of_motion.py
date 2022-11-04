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
        print(f"Количество свободных клеток: {number_of_remaining_cells}")
        while True:
            possible_values_lst = ["x", "0"]
            count = 0
            if current_gamer == gamer_1:
                value = "x"
                step = int(input(f"{current_gamer.capitalize()}, ваш ход: "))
            else:
                value = "0"
                current_gamer = gamer_2
                step = int(input(f"{current_gamer.capitalize()}, ваш ход: "))

            rendering_list(step_maps(struct_list(),step,value))
            
            if not value in possible_values_lst:
                print(f"\nОшибка. {current_gamer.capitalize()}, введите корректное значение: x или 0. Попробуйте еще раз:" )
                continue
            else:
                count += 1
                break
        number_of_remaining_cells -= count
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    print(f"Все свободные клетки закончились")

tic_tac_toe_with_2_players()