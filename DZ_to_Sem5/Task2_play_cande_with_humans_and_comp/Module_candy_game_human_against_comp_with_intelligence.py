def candy_game_human_against_comp_with_intelligence(rest_of_candy):
    from random import choice
    from random import randint

    gamer = input("Введите имя игрока: ")
    skynet = "великий и всемогущий искусственный интеллект Skynet"
    player_lst = [gamer, skynet]
    current_gamer = choice(player_lst)
    print("\nСейчас начнется жеребьевка за право первого хода!\n\n"
     f"Поздравляем, {current_gamer.capitalize()}, право первого хода предоставлено тебе!\n"
     f"Учти, что за один ход можно забрать не более чем 28 конфет.\n\n"
      "Россия вперед!!!!!!\n")
    
    while rest_of_candy > 0:
        print(f"Количество оставшихся конфет: {rest_of_candy}")
        while True:
            if current_gamer.capitalize() == gamer.capitalize():
                remains = int(input(f"Ход игрока {gamer.capitalize()} (1 - 28 конфет): "))
            else:
                if rest_of_candy < 29: remains = rest_of_candy
                else:
                    division = rest_of_candy // 28
                    remains = rest_of_candy - ((division*28)+1)
                while remains > 28 or remains < 1:
                    remains = randint(1,28)
                print(f"Ход игрока {skynet.capitalize()} (1 - 28 конфет): {remains}")             
            if 1 <= remains <= 28:
                break
            else: print(f"\nОшибка. {current_gamer.capitalize()}, введи корректное значение количества конфет от 1 до 28. Попробуй еще раз:" )                
        rest_of_candy -= remains
        current_gamer = skynet if current_gamer == gamer else gamer
    if current_gamer == gamer: print(f"Победил {skynet.capitalize()}")
    else: print(f"Победил {gamer.capitalize()}")