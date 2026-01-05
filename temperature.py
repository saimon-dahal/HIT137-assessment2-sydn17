import pandas as pd
import glob

files= glob.glob("temperatures/*.csv")

all_data= []
for file in files:
  df= pd.read_csv(file)
  all_data.append(df)
  
data= pd.concat(all_data, ignore_index= True)
