# 12. Для натурального n создать список, состоящий из элементов последовательности 3n + 1.
# Пример:
# - Для n = 6: [1, 4, 7, 10, 13, 16, 19]
# Усложнение:
# Создать список, где указанные числа будут стоять на соответствующих индексах,
# остальные элементы сделать нулевыми, т.е. для индекса 1, значение 1,
# для индекса 4, значение 4 и т.п.
#Пример:
#- Для n = 6: [0,1,0,0,4,0,0,7,0,0,10]

num=int(input('Ввидите N: '))  
num_list=[]                                              
                              
for i in range(num+5):        
    num_list.append(0)        
    num_list.append(i*3+1)    
    num_list.append(0)        
                              
print(num_list)