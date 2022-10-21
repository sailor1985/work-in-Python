# (Усложненное). Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Выделите необходимые действия, этапы алгоритма. Посмотрите какие из них уже
# решены в предыдущей задаче.
# Оформите необходимые функции в виде модуля и импортируйте.
# Примечание Многочлены в файлах могут быть разной степени

import Module1, Module2
from numpy import poly1d, polyadd

quantity1 = int(input("Введите степень 1 многочлена: "))
quantity2 = int(input("Введите степень 2 многочлена: "))

# 1. Формирование многочленов.
# Класс poly1d принимает коэффициенты или корни для инициализации и формирует полиномиальный объект.
# При печати его тип - polynomial

polynomial1 = poly1d(Module1.formation_of_random_coefficients(quantity1))
polynomial2 = poly1d(Module1.formation_of_random_coefficients(quantity2))

polynomial1_str = str(polynomial1)
polynomial2_str = str(polynomial2)

# 2. Запись в отдельные файлы сфомированные многочлены.
Module2.write_to_file(polynomial1_str, "test2.txt") #файл с многочленом номер 1
Module2.write_to_file(polynomial2_str, "test3.txt") #файл с многочленом номер 2

# 3. Расчет суммы 2х многочленов
sum_of_polynomial = polyadd(polynomial1, polynomial2)
sum_of_polynomial_str = str(sum_of_polynomial)

# 4. Запись в файл суммы многочленов многочленов.
Module2.write_to_file(sum_of_polynomial_str, "test4.txt") #файл с суммой 2х многочленов