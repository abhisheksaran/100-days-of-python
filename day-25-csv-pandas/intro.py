# import csv
#
#
# data_file = "weather_data.csv"
# with open(data_file, mode="r") as f:
#     lines = f.readlines()
#
# with open(data_file) as file:
#     data = csv.reader(file)
#     temperature = []
#     print(type(data))
#     for row in data:
#         if row[1] != 'temp':
#             temperature.append(row[1])
#
# print(temperature)

import pandas

data = pandas.read_csv("weather_data.csv")
temp = data["temp"]
print(type(temp))

# You can convert the series object into list data type
# And dataframe too can be converted into json, excel, dict etc.
temp_list = temp.to_list()

# To calculate the mean of column, you can usr the inbuilt mean method of Series class
print(sum(temp_list) / len(temp_list))
print(temp.mean())
print(temp.max())

# Can access the column in two ways
print(data["condition"])
print(data.condition)

# Filtering the data with condition
print("\nThe row with max temperature is:\n{}\n".format(data[data.temp == data.temp.max()]))

# Creating the dataframe from scratch
data_dict = {
    "students": ["Abhishek", "Rahul", "Sai"],
    "scores": [1, 2, 3]
}
data = pandas.DataFrame(data_dict)
print(type(data))
print(data)

# Saving dataframe to CSV
data.to_csv("scores.csv")
