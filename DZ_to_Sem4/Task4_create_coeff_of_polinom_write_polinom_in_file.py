# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# многочлена и записать в файл многочлен степени k.
# Коэффициенты должны быть случайными числами в диапазоне от 1 до 100

# Пример:
# - k=2 => 6*x^2 + 4*x + 5 = 0 или x^2 + 5 = 0 или 10*x^2 = 0
# Усложнение: Коэффициенты в полиноме могут быть нулевыми.

# Примечание Создать три функции:

# 1) Функция формирования полинома. аргумент: степень полинома; возвращает полином.
# Коэффициенты вычисляются случайными.
# Полином удобно представить как словарь или как список коэффициентов. (на ваш выбор)
# В словаре степени будут ключами, в списке - индексами.
# Например k=3 => 6*x^3 + 4*x + 5. Словарь будет такой: {3:6, 2:0, 1:4, 0:5}.
# А список такой [5,4,0,6]
# 2) Функция формирование строки-полинома. Аргумент: полином (в вид словаря или списка).
# Возвращает строку вида '6*x^3 + 4*x + 5'
# Примечание: Обратите внимание на запись первой и нулевой степени, а также учетнулевого коэффициента.
# Для формирования строки удобно использовать join
# 3) Функция записи строки-полинома в файл. Аргументы: имя файла и строка-полином

from random import randint

def create_coeffs(num: int) -> list:   #Формирование случайных чисел/коэффициентов:
                                        #Вход: число k: 1-100
                                        #Выход: список коэффициентов-последовательностьх
    return [randint(1, 100) for _ in range(num + 1)]

def create_str(list_coeff: list) -> str:  #Формирование текстовой строки:
                                        #Вход: последовательность []
                                        #Выход: строка
    lenght = len(list_coeff)
    lst_str = [f"{el}*x^{lenght - idx - 1}" for idx, el in enumerate(list_coeff)]
    return " + ".join(lst_str)

def write_to_file(polynom_string, filename):  #Запись в текстовый файл. Вход:строка
    with open(filename, mode="w", encoding="utf-8") as file:
        file.write(polynom_string)

write_to_file(create_str(create_coeffs(10)), "test.txt")