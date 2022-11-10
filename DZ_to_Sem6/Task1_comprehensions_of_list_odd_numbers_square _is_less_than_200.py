# 1. Сформировать список нечетных целых чисел от 0 до N, квадрат которых меньше 200.
# Использовать comprehensions

num_list = [] 
N = int(input(f"Введите число N:"))
num_list =[i for i in [i for i in range(N+1)] if i % 2 != 0 and i**2 < 200] 
print(num_list)