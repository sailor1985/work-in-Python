# Создание frontend модуля: все, что связано с прорисовкой поля

import Module_rendering_function_with_Texttable as render
import Module_data_structure_dictionary as D

#Вызов функции отрисовки поля клеток, принимающей текущее состояние системы:
#рандомные значения: "X", "", "0"
render.rendering(D.struct_dic()) 