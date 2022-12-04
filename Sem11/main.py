import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Air_Traffic_Passenger_Statistics_1.csv", delimiter=",")

#1. Фильтрация данных:
df.activity_Period #  Фильтрация по столлбцу activity_Period
df["Passenger Count"] #  Фильтрация по столлбцу Passenger Count
df["Operating Airline"] == "ATA Airlines" #  Фильтрация  по совпадению условия, вывод:True(совпало)/False(нет)
df[df["Operating Airline"] == "ATA Airlines"]  #  Фильтрация  по совпадению условию

#2. Построение графика по числовым значениям + по отфильтрованным значениям
dfATA = df[df["Operating Airline"] == "ATA Airlines"]
dfAC = df[df["Operating Airline"] == "Air Canada"]
dfAWA = df[df["Operating Airline"] == "WestJet Airlines"]