# 1. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов
# списка, стоящих на нечётной позиции.
# Пример:    
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

length = int(input("Введите количество чисел в списке: "))
num_list= []

for i in range(length):
    element = int(input("Введите числа списка: "))
    num_list.append(element)
print(f"Заданный список следующий: \n {num_list}")

 
# print(num_list)
# sum = sum(num_list)
# print(f"Сумма чисел в последовательности, отображенной выше, равна {sum}")


# def Method(numberA):
#     fact = 1
#     for i in range(1, numberA + 1):  
#         fact = fact * i
#     return fact


# Console.WriteLine("Введите число: ");
# string number = Console.ReadLine()!;
# int a;

# bool result = int.TryParse(number, out a);
# if (result)
# {
#     Console.WriteLine("Значение числа введено корректно");
#     int res = 2;
#     int count = a;
#     if (count % 2 == 1 & res < count)
#     {
#         count--;  
#         while (count % 2 == 0 & res <= count)
#         {
#         }
#     }
#     else
#     {
#         while (count % 2 == 0 & res <= count)
#         {
#             Console.WriteLine(res);
#             res = res+2;
#         }     
#     }
# }
# else
#     {
#         Console.WriteLine("Некорректный ввод данных");
#     }        Console.WriteLine(res);
#              res = res + 2;  
    