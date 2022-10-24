from random import choice
count_of_sticks = int(input('введите количество палочек для игры: '))
gamer_1, gamer_2 = input('введите имя 1 игрока: '), input('введите имя 2 игрока: ')
player_lst = [gamer_1, gamer_2]
current_gamer = choice(player_lst)
print(current_gamer)

if current_gamer == gamer_1:
    while count_of_sticks > 0:
        print('количество оставшихся палочек: {}'.format(count_of_sticks))
        while True:
            number_to_delete = int(input('ход игрока {} (1 - 3): '.format(current_gamer)))
            if number_to_delete >= 1 and number_to_delete <= 3:
                break
        count_of_sticks -= number_to_delete
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    if current_gamer == gamer_1:
        print('Победил {}'.format(gamer_2))
    else: print('Победил {}'.format(gamer_1))
else: gamer_2