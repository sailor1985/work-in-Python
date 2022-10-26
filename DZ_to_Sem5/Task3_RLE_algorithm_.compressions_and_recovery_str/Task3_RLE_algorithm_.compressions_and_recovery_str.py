# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# https://ru.wikipedia.org/wiki/Кодированиедлинсерий

# Создать функцию сжатия строки и функцию восстановления строки.

# Пример:
# ABCABCABCDDDFFFFFF ->1A1B1C1A1B1C1A1B1C3D6F -> ABCABCABCDDDFFFFFF
# WWJJJHDDDDDPPGRRR -> 2W3J1H5D2P1G3R -> WWJJJHDDDDDPPGRRR

#1. Функция сжатия строки
string_input = "ABCABCABCDDDFFFFF"

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

print(f"Закодированная строка: {encode(string_input)}")

#2. Функция восстановления строки
encoded_string = "1A1B1C1A1B1C1A1B1C3D5F"

def decode(string):
    decoded_message = ""
    i = 0
    j = 0
    # разделение закодированного сообщения
    while (i <= len(string) - 1):
        count = int(string[i])
        word = string[i + 1]
        # отображение символа несколько раз в соответствии с счетчиком
        for j in range(count):
            # объединяется с декодированным сообщением
            decoded_message += word
            j += 1
        i += 2
    return decoded_message

print(f"Раскодированная строка: {decode(encoded_string)}")