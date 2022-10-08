#5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#*Пример:*

#- A (3,6); B (2,1) -> 5,09
#- A (7,-5); B (1,-1) -> 7,21
#Если вы не знаете как вычислить квадратный корень, оставьте квадрат расстояния

import math


x1 = int(input("Введите координаты X1:  "))
y1 = int(input("Введите координаты Y1:  "))

x2 = int(input("Введите координаты X2:  "))
y2 = int(input("Введите координаты Y2:  "))

result = round(math.sqrt((x2-x1)**2 + (y2-y1)**2), 2)
print(f"Расстояние между двумя точками с координатами ({x1},{y1}) и ({x2},{y2}) равно в 2D пространстве {result}")