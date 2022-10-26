# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# https://ru.wikipedia.org/wiki/Кодированиедлинсерий

# Создать функцию сжатия строки и функцию восстановления строки.

# Пример:
# ABCABCABCDDDFFFFFF ->1A1B1C1A1B1C1A1B1C3D6F -> ABCABCABCDDDFFFFFF
# WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR

string_input = "ABCABCABCDDDFFFFF"
string_output = ""

#1. Функция сжатия строки
def encode(string):
    encoded_string = ""
    i = 0
    while (i <= len(string) - 1):
        count = 1
        char = string[i]
        j = i
        while j < len(string) - 1:
            if string[j] == string[j + 1]:
                count += 1
                j += 1
            else:
                break
        encoded_string += str(count) + char
        i = j + 1
    return encoded_string

print(encode(string_input))
