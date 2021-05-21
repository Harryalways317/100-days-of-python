
import pandas as pd

squirrel_data = pd.read_csv("Squirrel_Data.csv")
grey_color = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Gray"])
cinnamon_color = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Cinnamon"])
black_color = len(squirrel_data[squirrel_data['Primary Fur Color'] == "Black"])
print(grey_color)
print(cinnamon_color)
print(black_color)
data_dict = {
  "Fur color" : ["Gray","Cinnamon","Black"],
  "count" : [grey_color,cinnamon_color,black_color]
}
data = pd.DataFrame(data_dict)
data.to_csv("Squirrel_color.csv")
