# import csv

# with open("./day25/weather.csv") as data_file:
#     data= csv.reader(data_file)
#     temperatures= []
#     for row in data:
#         if row[1] !='temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)


import pandas
import numpy as np
data=pandas.read_csv("./day25/weather.csv")

dict=data.to_dict()
print(dict)

temp=data["temp"]
print(temp.max())

print(data[data.day=='Monday'])

print(data[data.temp==data.temp.max()])

monday= data[data.day=='Monday']
print(monday.condition)

print(int(monday.temp) * 9/5 +32)

#dataframe

data_dict = {
    "students":['kidist','daniel','kidu'],
    "score":[99,90,98]
}

mark = pandas.DataFrame(data_dict)

mark.to_csv("./day25/marksheet.csv")