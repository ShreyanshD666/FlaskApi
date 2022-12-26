import pandas as pd

df = pd.read_csv("finalGravityStars.csv")
df.head()

name = df["Star_name"].to_list()
mass = df["Mass"].to_list()
radius = df["Radius"].to_list()
dist = df["Distance"].to_list()
gravity = df["Gravity"].to_list()

finalStarList = []

temp_dict ={}
for i in range(0,len(name)):
    temp_dict["name"]=name[i]
    temp_dict["mass"]=mass[i]
    temp_dict["radius"]=radius[i]
    temp_dict["distance"]=dist[i]
    temp_dict["gravity"]= gravity[i]
    finalStarList.append(temp_dict)
    temp_dict ={}
    
print(finalStarList)