from random import choice
from Module_rendering_function_with_Texttable import rendering_list, step_maps

def tic_tac_toe_with_2_players(number_of_cells = 9): #Функция игры 2 игроков
    gamer_1, gamer_2 = input("Введите имя 1 игрока (рисует x): "), input("Введите имя 2 игрока (рисует 0): ")
    player_lst = [gamer_1, gamer_2]
    current_gamer = choice(player_lst)
    print("\nСейчас начнется жеребьевка за право первого хода!\n\n"
     f"Поздравляем, {current_gamer.capitalize()}, право первого хода предоставлено вам!\n")
    print("Текущее состояние поля клеток")
    maps = list(range(1,10))
    rendering_list(maps)
    
    while number_of_cells != 0:
        print(f"Количество оставшихся ячеек: {number_of_cells}")
        count = 0
        while True:
            if current_gamer == gamer_1: value = "x"
            else: value = "0"
            # Проверка корректности ввода номера ячейки
            valid = False
            while not valid:
                step = input(f"{current_gamer.capitalize()}, выберите ячейку, в которую хотите поставить ваш знак: ")
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
            rendering_list(step_maps(maps,step,value))
            count += 1
            number_of_cells -= count
            current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    print("Ячейки закончились")

tic_tac_toe_with_2_players()