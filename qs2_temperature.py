# pandas for data analysis
# glob for finding multiple csv files

import pandas as pd
import glob

files= glob.glob("temperatures/*.csv")

all_data= []

# read each csv file and store
for file in files:
  df= pd.read_csv(file)
  all_data.append(df)
  
#all csv into single dataframe  
data= pd.concat(all_data, ignore_index= True)

months= [
  "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]

#convert wide format to long format
data_long= data.melt(
  id_vars= ["STATION_NAME"],  #station name fixed
  value_vars= months,  #cnvert month columns
  var_name= "Month",  #column for month names
  value_name= "Temperature"  #column for temperature values
)
#convrt temperature value to numeric
data_long["Temperature"]=pd.to_numeric(
  data_long["Temperature"], errors="coerce"
)
#function to map months to Australian season
def get_season(month):
  if month in ["December", "January", "February"]:
    return "Summer"
  elif month in ["March", "April", "May"]:
    return "Autumn"
  elif month in["June", "July", "August"]:
    return "Winter"
  else:
    return "Spring"
#apply season classification to each row
data_long["Season"]= data_long["Month"].apply(get_season)

#calculate average temperature for each season
seasonal_avrg= (
  data_long.dropna(subset=["Temperature"])
  .groupby("Season")["Temperature"]
  .mean()
)
#save to a text file
with open ("average_temp.txt", "w") as f:
  for season in ["Summer", "Autumn", "Winter", "Spring"]:
    f.write(f"{season}: {seasonal_avrg[season]:.1f}°C\n")

#calculate temperature statistics
station_stats= (
  data_long.dropna(subset=["Temperature"])
  .groupby("STATION_NAME")["Temperature"]
  .agg(["min", "max", "std"])
)
#calculaate temperature range
station_stats["range"]= station_stats["max"] - station_stats["min"]
#find station with largest range
max_range= station_stats["range"].max()
largest_range= station_stats[station_stats["range"] ==max_range]

#save to text file
with open ("largest_temp_range_station.txt", "w") as f:
  for station, row in largest_range.iterrows():
    f.write(
      f"{station}: Range {row['range']:.1f}°C"
      f"(Max: {row['max']:.1f}°C, Min: {row['min']:.1f}°C\n"
    )

#identify most stable and variable stations using standard deviation
min_std= station_stats["std"].min()
max_std= station_stats["std"].max()

most_stable= station_stats[station_stats["std"] == min_std]
most_variable= station_stats[station_stats["std"] == max_std]

#save the result
with open ("temperature_stability_stations.txt", "w") as f:
  for station, row in most_stable.iterrows():
    f.write(f"Most stable: {station}: StdDev {row['std']:.1f}°C\n")
  for station, row in most_variable.iterrows():
    f.write(f"Most variable: {station}: StdDev {row['std']:.1f}°C\n")

print("Analysis complete")
  
