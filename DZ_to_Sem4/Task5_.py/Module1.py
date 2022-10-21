from random import randint

def formation_of_random_coefficients(num: int) -> list:   #Формирование случайных чисел/коэффициентов:
                                        #Вход: число k: 1-100
                                        #Выход: список коэффициентов-последовательностьх
    return [randint(1, 100) for _ in range(num + 1)]