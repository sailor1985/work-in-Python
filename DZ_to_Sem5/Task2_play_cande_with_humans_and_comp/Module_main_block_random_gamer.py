def main_block_random_gamer(current_gamer, gamer_1, gamer_2, rest_of_candy):
    while rest_of_candy > 0:
        print(f"Количество оставшихся конфет: {rest_of_candy}")
        while True:
            remains = int(input(f"Ход игрока {current_gamer} (1 - 3): "))
            if remains >= 1 and remains <= 3:
                break
        rest_of_candy -= remains
        current_gamer = gamer_2 if current_gamer == gamer_1 else gamer_1
    if current_gamer == gamer_1:
        print(f"Победил {gamer_2}")
    else: print(f"Победил {gamer_1}")