# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('\nУтверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \nпри (X; Y; Z):\n')
for x in range(2):
    for y in range(2):
        for z in range(2):
            if (not (x or y or z) == (not x and not y and not z)):
                print(f'({x}; {y}; {z}) -> истинно')
            else:
                print(f'\n{x}; {y}; {z}) -> ложно')
