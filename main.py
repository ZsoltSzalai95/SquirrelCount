# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
#

#________________________Reading data with CSV:
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1] != "temp":
#             temperature.append(int(row[1]))
# #     print(temperature)
#________________________Data analysis with pandas:
# import pandas
#
# data= pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# #
# # # data_dict = data.to_dict()
# # # print(data_dict)
# #
# # temp_list = data["temp"].to_list()
# average= sum(temp_list)/len(temp_list)
# print(average) # print(data["temp"].mean())
#
# result = data["temp"].max()
# print(result)
#
# # #Get Data in columns:
# # print(data["temp"])
# # print(data.temp)

#Get data in rows:
# print(data[data.day == "Monday"])

# # print(data[data.temp == data.temp.max()])
#
# monday=data[data.day=="Monday"]
# print((monday.temp)*9/5 + 32)

#__________________________: Squirrel data start here:

import pandas
data = pandas.read_csv("2018_Squirrel_data.csv")
gray_color_count = len(data[data["Primary Fur Color"] == "Gray"])
red_color_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_color_count = len(data[data["Primary Fur Color"] == "Black"])

print(f"{gray_color_count} gray squirrel")
print(f"{red_color_count} red squirrel")
print(f"{black_color_count} black squirrel")


data_dict={
    "Fur Color" : ["Gray", "Cinnamon", "Black",],
    "Count": [gray_color_count, red_color_count, black_color_count]
}
df= pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")



