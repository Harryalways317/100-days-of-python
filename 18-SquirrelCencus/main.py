import pandas as pd

squirrel_data = pd.read_csv("Squirrel_Data.csv")
print(squirrel_data)
color = squirrel_data['Primary Fur Color']