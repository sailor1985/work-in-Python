def candy_game_with_2_humans(rest_of_candy):
    from random import choice
    import Module_main_block_random_gamer as main
    gamer_1, gamer_2 = input('Введите имя 1 игрока: '), input('Введите имя 2 игрока: ')
    player_lst = [gamer_1, gamer_2]
    current_gamer = choice(player_lst)
    print("\nСейчас начнется жеребьевка за право первого хода!\n\n"
     f"Поздравляем, {current_gamer.capitalize()}, право первого хода предоставлено тебя!\n"
     f"Учти, что за один ход можно забрать не более чем 28 конфет.\n\n"
      "Россия вперед!!!!!!\n")
    if current_gamer.capitalize() == gamer_1.capitalize():
        main.main_block_random_gamer(current_gamer.capitalize(), gamer_1.capitalize(), gamer_2.capitalize(), rest_of_candy)
    else:
        current_gamer.capitalize() == gamer_2.capitalize()
        main.main_block_random_gamer(current_gamer.capitalize(), gamer_1.capitalize(), gamer_2.capitalize(), rest_of_candy)