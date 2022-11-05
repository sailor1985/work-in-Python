from Module_rendering_function_with_Texttable import rendering_list

def singlegame(curplayer): 
    # Representing the Tic-Tac-Toe 
    val = [' ' for i in range(9)] 
      
    # Storing the positions occupied by X and O 
    playerpos = {'X' : [], 'O' : []} 


maps = list(range(1,10))
print(maps)

def take_input(player_token: str):
    valid = False
    while not valid:
        player_answer = input("Куда поставим " + player_token+"? ")
        try:
            player_answer = int(player_answer)
        except:
            print("Некорректный ввод. Вы уверены, что ввели число?")
            continue
        if player_answer >= 1 and player_answer <= 9:
            if (str(maps[player_answer-1]) not in "XO"):
                maps[player_answer-1] = player_token
                valid = True
            else:
                print("Эта клеточка уже занята")
        else:
            print("Некорректный ввод. Введите число от 1 до 9 чтобы походить.")

take_input("x")
# rendering_list()
