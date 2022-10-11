# 2. Напишите программу, которая принимает на вход число N и выдает
# набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input(f"Введите число N: "))

def Method(numberA):
    fact = 1
    for i in range(1, numberA + 1):  
        fact = fact * i
    return fact

composition = Method(number)
print(f"Набор произведений чисел от 1 до {number} равен {composition}")