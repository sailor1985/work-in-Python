def candy_game_with_2_humans(rest_of_candy):
    from random import choice
    gamer_1, gamer_2 = input('Введите имя 1 игрока: '), input('Введите имя 2 игрока: ')
    player_lst = [gamer_1, gamer_2]
    current_gamer = choice(player_lst)
    print(current_gamer)
    if current_gamer == gamer_1:
        while rest_of_candy > 0:
            print('количество оставшихся палочек: {}'.format(rest_of_candy))
            while True:
                remains = int(input('ход игрока {} (1 - 3): '.format(current_gamer)))
                if remains >= 1 and remains <= 3:
                    break
            rest_of_candy -= remains
            current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
        if current_gamer == gamer_1:
            print('Победил {}'.format(gamer_2))
        else: print('Победил {}'.format(gamer_1))
    else:
        current_gamer == gamer_2
        while rest_of_candy > 0:
            print('количество оставшихся палочек: {}'.format(rest_of_candy))
            while True:
                remains = int(input('ход игрока {} (1 - 3): '.format(current_gamer)))
                if remains >= 1 and remains <= 3:
                    break
            rest_of_candy -= remains
            current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
        if current_gamer == gamer_1:
            print('Победил {}'.format(gamer_2))
        else: print('Победил {}'.format(gamer_1))

candy_game_with_2_humans(10)