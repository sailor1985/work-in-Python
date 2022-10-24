# 2. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит некоторое кол-во конфет, например 220.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

# Подумайте об алгоритме игры. Здесь есть ключевые числа количества конфет, которые
# точно определят победу.

from random import choice, randint
import Module_of_first_move_player as player
import Module_correct_input as correct
import Module_of_first_move_bot as bot

print("\nGAME: HUMAN AGAINST COMPUTER\n")
# human_name = input("Введите имя игрока:  ")
# skynet = "великий и всемогущий искусственный интеллект Skynet"
# print(f"\nПривет {human_name.capitalize()}!\n")
# print(f"Против тебя, {human_name.capitalize()}, играет {skynet}\n"
#        "\nПрочти внимательно условия игры:\n\n"
#       f"На столе лежит 220 конфет. Ты, {human_name.capitalize()}, и {skynet}\n"
#        "делаете ход друг после друга. Первый ход определяется жеребьёвкой.\n"
#        "За один ход можно забрать не более чем 28 конфет\n"
#        "Все конфеты оппонента достаются сделавшему последний ход. \n")
print("Начнем жеребьевку?\n")
correct.correct_input() #Функция проверки коорректности ввода согласия на начало жеребьевки

# player_lst = [human_name, skynet]
# current_player = choice(player_lst)
print("Сейчас начнется жеребьевка за право первого хода!\n\n"
     f"Поздравляем, {current_player.capitalize()}, право первого хода предоставлено тебя!\n"
     f"Учти, что за один ход можно забрать не более чем 28 конфет.\n\n"
      "Россия вперед!!!!!!\n")

if current_player.capitalize() == human_name.capitalize(): player.player_first_move(human_name.capitalize(), skynet, 10)
else: bot.bot_first_move(human_name.capitalize(), skynet, 10)