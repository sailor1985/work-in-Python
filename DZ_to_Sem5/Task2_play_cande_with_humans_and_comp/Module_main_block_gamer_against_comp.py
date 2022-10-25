from random import randint

def main_block_gamer_against_comp(current_gamer, gamer, skynet, rest_of_candy):
    while rest_of_candy > 0:
        print(f"Количество оставшихся конфет: {rest_of_candy}")
        while True:
            if current_gamer == gamer:
                remains = int(input(f"Ход игрока {gamer} (1 - 28 конфет): "))
            else:
                remains = randint(1, 28)
                print(f"Ход игрока {skynet} (1 - 28 конфет): {remains}")
            if remains >= 1 and remains <= 28:
                break
        rest_of_candy -= remains
        current_gamer = skynet if current_gamer == gamer else gamer
    if current_gamer == gamer:
        print(f"Победил {skynet}")
    else: print(f"Победил {gamer}")