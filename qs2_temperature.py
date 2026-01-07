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
  
