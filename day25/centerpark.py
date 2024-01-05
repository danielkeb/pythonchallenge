import pandas as pd

data= pd.read_csv("./day25/centralpark.csv")

grey= len(data[data["Primary Fur Color"] == "Gray"])
cinnamon= len(data[data["Primary Fur Color"] == "Cinnamon"])
black= len(data[data["Primary Fur Color"] == "Black"])




data_dict={
    "Fur Color": ["Gray","Cinnamon","black"],
    "Count":[grey,cinnamon,black]
}


dict=pd.DataFrame(data_dict)

df=dict.to_csv("./day25/color.csv")