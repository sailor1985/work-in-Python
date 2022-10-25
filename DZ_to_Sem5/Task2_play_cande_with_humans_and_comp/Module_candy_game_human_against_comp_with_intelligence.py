def candy_game_with_comp(rest_of_candy):
    from random import choice
    import Module_main_block_gamer_against_comp as main
    
    gamer = input("Введите имя игрока: ")
    skynet = "великий и всемогущий искусственный интеллект Skynet"
    player_lst = [gamer, skynet]
    current_gamer = choice(player_lst)
    print("\nСейчас начнется жеребьевка за право первого хода!\n\n"
     f"Поздравляем, {current_gamer.capitalize()}, право первого хода предоставлено тебе!\n"
     f"Учти, что за один ход можно забрать не более чем 28 конфет.\n\n"
      "Россия вперед!!!!!!\n")
    if current_gamer.capitalize() == gamer.capitalize():
        main.main_block_gamer_against_comp(current_gamer.capitalize(), gamer.capitalize(), skynet.capitalize(), rest_of_candy)
    else:
        current_gamer.capitalize() == skynet.capitalize()
        main.main_block_gamer_against_comp(current_gamer.capitalize(), gamer.capitalize(), skynet.capitalize(), rest_of_candy)        