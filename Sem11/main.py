import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Air_Traffic_Passenger_Statistics_1.csv", delimiter=",")

#1. Фильтрация данных:
# df.activity_Period #  Фильтрация по столбцу "activity_Period" и вывод в консоль
# df["Passenger Count"] #  Фильтрация по столбцу "Passenger Count" и вывод в консоль
# df["Operating Airline"] == "ATA Airlines" #  Фильтрация  по совпадению условия, вывод:True(совпало)/False(нет) и вывод в консоль
# df[df["Operating Airline"] == "ATA Airlines"]  #  Фильтрация  по совпадению условию и вывод в консоль

dfATA = df[df["Operating Airline"] == "ATA Airlines"]
dfAC = df[df["Operating Airline"] == "Air Canada"]
dfAWA = df[df["Operating Airline"] == "WestJet Airlines"]

#2. Построение графика по числовым значениям + по отфильтрованным значениям
fig, ax = plt.subplots()
plt.plot(dfATA.activity_Period, dfATA["Passenger Count"])
plt.show()
