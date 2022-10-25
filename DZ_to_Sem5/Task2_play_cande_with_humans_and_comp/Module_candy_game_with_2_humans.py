def candy_game_with_2_humans(rest_of_candy):
    from random import choice
    
    gamer_1, gamer_2 = input("Введите имя 1 игрока: "), input("Введите имя 2 игрока: ")
    player_lst = [gamer_1, gamer_2]
    current_gamer = choice(player_lst)
    print("\nСейчас начнется жеребьевка за право первого хода!\n\n"
     f"Поздравляем, {current_gamer.capitalize()}, право первого хода предоставлено тебя!\n"
     f"Учти, что за один ход можно забрать не более чем 28 конфет.\n\n"
      "Россия вперед!!!!!!\n")

    while rest_of_candy > 0:
        print(f"Количество оставшихся конфет: {rest_of_candy}")
        while True:
            remains = int(input(f"Ход игрока {current_gamer.capitalize()} (1 - 28 конфет): "))
            if 1 <= remains <= 28:
                break
            else: print(f"\nОшибка. {current_gamer.capitalize()}, введи корректное значение количества конфет от 1 до 28. Попробуй еще раз:" )                
        if remains > rest_of_candy:
            print(f"\nОшибка. {current_gamer.capitalize()}, введи корректное значение количества конфет от 1 до 28, которое меньше или равно количеству оставшихся конфет: {rest_of_candy}. Попробуй еще раз:" )                      
            continue
        rest_of_candy -= remains
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    if current_gamer == gamer_1: print(f"Победил {gamer_2.capitalize()}")
    else: print(f"Победил {gamer_1.capitalize()}")