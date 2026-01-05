import pandas as pd
import glob

files= glob.glob("temperatures/*.csv")

all_data= []
for file in files:
  df= pd.read_csv(file)
  all_data.append(df)
  
data= pd.concat(all_data, ignore_index= True)

months= [
  "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"
]
data_long= data.melt(
  id_vars= ["STATION_NAME"],
  value_vars= months,
  var_name= "Month",
  value_name= "Temperature"
)
data_long["Temperature"]=pd.to_numeric(
  data_long["Temperature"], errors="coerce"
)
