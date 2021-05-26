import csv
import pandas as pd
import numpy as np

#Dataframe with index, id_species, species_name, Images (number of images) sorted by decreasing number of images 
url = 'https://raw.githubusercontent.com/GFouilhe-AThiriet/Projet-L3/main/data.csv'
data = pd.read_csv(url)

species_name=data.species_name.to_numpy()

L=[]
for i in range (len(data)):
    species_group=""
    j=0
    while species_name[i][j]!="_":
        species_group=species_group+species_name[i][j]
        j=j+1
    L+=[species_group]

group = pd.Series(L)
a=[]
for i in range(len(L)):
    interrupteur=0
    for j in range(len(a)):
        if a[j]==L[i]:
                interrupteur=1
    if interrupteur==0:
        a+=[L[i]]

print(a)
print(len(a))

# data = pd.read_csv('data.csv')
# data.insert(2, "species_group", group)

# data.to_csv("groups",index=False)