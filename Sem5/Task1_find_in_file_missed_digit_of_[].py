# В файле находится N натуральных чисел, записанных через пробел
# Среди чисел не хватает одного, чтобы выполнялось условие А[i]-1 = А[i-1]. Найдите это число
# Для работы с файлами используйте менеджер контекста

def read_data(filename: str) -> list:
    with open(filename, "r", encoding = "utf-8") as data:
        a = data.read().split()
        a = list(map(int,a)) #  или  a = [int(elem) for elem in a]
    return a
    
a = read_data("file1.txt")

def check_data(a: list) -> int:
    for i in range(1,len(a)):
        if a[i] - 1 != a[i-1]:
            return a[i] - 1
print(check_data(a))