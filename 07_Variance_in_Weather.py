import pandas as pd
import numpy as np
from weather_data import london_data

print(london_data.head())
print(london_data.iloc[100:200])
print(len(london_data))

# Looking At Temperature
temp = london_data['TemperatureC']
average_temp = np.mean(temp)
var_temp = np.var(temp)
std_temp = np.std(temp)
print(average_temp)
print(var_temp)
print(std_temp)

# Filtering by month
june = london_data.loc[london_data["month"] == 6]["TemperatureC"]
july = london_data.loc[london_data["month"] == 7]["TemperatureC"]
print(np.mean(june))
print(np.mean(july))
print(np.std(june))
print(np.std(july))

for i in range(1, 13):
  month = london_data.loc[london_data["month"] == i]["TemperatureC"]
  print("The mean temperature in month "+str(i) +" is "+ str(np.mean(month)))
  print("The standard deviation of temperature in month "+str(i) +" is "+ str(np.std(month)) +"\n")
