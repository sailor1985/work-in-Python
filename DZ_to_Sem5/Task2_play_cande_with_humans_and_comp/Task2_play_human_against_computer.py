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

import Module_correct_input_draw as draw
import Module_candy_game_with_2_humans as humans
import Module_candy_game_human_against_comp as comp
import Module_candy_game_human_against_comp_with_intelligence as intelligence

print("\nTHE CANDY GAME\n")
print("Начнем жеребьевку?\n")
draw.correct_input() #Функция проверки коорректности ввода согласия на начало жеребьевки

#1. Игра с конфетами: человек против человека
humans.candy_game_with_2_humans(220)

#2. Игра с конфетами: человек против бота
comp.candy_game_with_comp(220)

#3. Игра с конфетами: человек против бота с интеллектом
intelligence.candy_game_human_against_comp_with_intelligence(220)