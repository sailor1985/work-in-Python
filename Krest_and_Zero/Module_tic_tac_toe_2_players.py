from random import choice
from Module_rendering_function_with_Texttable import rendering_list
from Module_correctness_input_data import valid_input
import keyboard

def two_players(number_of_cells = 9): #Функция игры 2 игроков
    gamer_1, gamer_2 = input("Введите имя 1 игрока (рисует x): "), input("Введите имя 2 игрока (рисует 0): ")
    player_lst = [gamer_1, gamer_2]
    current_gamer = choice(player_lst)
    print("\nСейчас начнется жеребьевка за право первого хода!\n\n"
     f"Поздравляем, {current_gamer.capitalize()}, право первого хода предоставлено вам!\n")
    
    maps = list(range(1,10)) #Структура хранения данных (список), заполненная цифрами в диапозоне от 1 до 9.
                             #Игрок вводит цифру из этого диапозона тем самым показывая в какую ячейку
                             #поставить свой знак: x или 0

    print("Текущее состояние поля клеток")
    rendering_list(maps) # Функция рисования исходного состояния поля клеток
  
    while number_of_cells != 0:
        print(f"Количество оставшихся ячеек: {number_of_cells}")
        count = 0
        print("Чтобы прервать игру нажмите клавишу q, продолжить - пробел: ")
        if keyboard.read_key() == "q": #Функция прерывания игроком игры ее начала
            print("Игра прервана игроком")
            break
 
        if current_gamer == gamer_1: value = "x"
        else: value = "0"
        if keyboard.read_key() == "q": #Функция прерывания игроком игры до своего хода
            print("Игра прервана игроком")
            break

        valid_input(current_gamer, maps, value) #Функция проверки корректности ввода данных. В ней же функция заполнения
                                                #списка крестиком или ноликом
                               
        rendering_list(maps)  # Функция рисования текущего состояния поля клеток с учетом введенных ранее символов  
        count += 1             
        number_of_cells -= count
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    print("Игра завершена")