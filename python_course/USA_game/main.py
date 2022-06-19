# import csv

# with open("python_course/USA_game/weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)

# import pandas
# data = pandas.read_csv("python_course/USA_game/weather_data.csv")
# avg_temp = data["temp"].mean()

# # col = data[data.temp == data.temp.max()]
# # print(col)
    
# monday = data[data.day == "Monday"]
# print(9/5*int(monday.temp)+32)

# squirrel data

import pandas

data = pandas.read_csv("python_course/USA_game/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

color = data["Primary Fur Color"]

color_based_amount = pandas.DataFrame({
    "Fur Color":["grey", "red", "black"],
    "Count":[len(data[color=="Gray"]), len(data[color=="Cinnamon"]), len(data[color=="Black"])]
})

color_based_amount.to_csv("python_course/USA_game/squirrel_count.csv")