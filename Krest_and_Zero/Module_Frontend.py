# Создание frontend модуля: все, что связано с прорисовкой поля

import Module_rendering_function_with_Texttable as render
import Module_data_structure as D

# Этап 1:
#Вызов функции отрисовки поля клеток, принимающей текущее состояние системы:
#рандомные значения: "X", "", "0"
render.rendering_random_dic(D.struct_random_dic()) 