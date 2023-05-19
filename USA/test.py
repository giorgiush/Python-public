# import csv
# x = 0
# temps = []
# with open("./day_25_US_States/weather_data.csv", mode="r") as file:
#     data = csv.reader(file)
#     for i in data:
#         if x == 0:
#             x += 1
#             continue
#         temps.append(int(i[1]))

# print(temps)

# import pandas

# data = pandas.read_csv("./day_25_US_States/weather_data.csv")
# roww = (data[data["temp"] == data["temp"].max()])
# print(roww)

# smthng = {
#     "name": ["a", "b", "c"],
#     "score": [1, 2, 3]
# }

# import pandas
# dt = pandas.DataFrame(smthng)
# dt.to_csv("./day_25_US_States/new_data.csv")

# import pandas

# data = pandas.read_csv("./day_25_US_States/squirrels_data.csv")
# ls_gray = len((data[data["Primary Fur Color"] == "Gray"]))
# ls_black = len((data[data["Primary Fur Color"] == "Black"]))
# ls_cinnamon = len((data[data["Primary Fur Color"] == "Cinnamon"]))

# results = {
#     "Fur Color": ["gray", "black", "cinnamon"],
#     "count": [ls_gray, ls_black, ls_cinnamon]
# }

# final = pandas.DataFrame(results)
# print(final)




