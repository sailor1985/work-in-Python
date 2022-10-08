#3. Напишите программу, которая принимает на вход координаты точки (X и Y),
#причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится
#эта точка (или на какой оси она находится).
#*Пример:*

#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

while True:
    try:
        coordinateX = int(input("Введите координату X точки: "))    
        break
    except ValueError:
        print("Не корректный ввод данных.Вы ввели не число. Попробуйте снова: ")

while True:
    try:
        coordinateY = int(input("Введите координату Y точки: "))    
        break
    except ValueError:
        print("Не корректный ввод данных.Вы ввели не число. Попробуйте снова: ")

def QuarterNumber(x, y):
    if (x > 0 and y > 0):
        print("1 четверть")
    elif (x < 0 and y > 0):
        print("2 четверть")
    elif (x < 0 and y < 0):
        print("3 четверть")
    elif (x > 0 and y <0 ):
        print("4 четверть")

QuarterNumber(coordinateX, coordinateY)