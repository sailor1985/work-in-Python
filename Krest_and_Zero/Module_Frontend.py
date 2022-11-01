# Создание frontend модуля: все, что связано с прорисовкой поля
import Module_data_structure as str
import Module_rendering_function_with_Texttable as render

dictinary = str.structure() #Вызов функции заполнения структуры данных (словарь)
render.rendering(dictinary) #Вызов функции отрисовки поля клеток с рандомными значениями: "X", "", "0" 