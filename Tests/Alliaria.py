import os
import pandas as pd

url = 'https://raw.githubusercontent.com/GFouilhe-AThiriet/Projet-L3/main/Miscellaneous/groups.csv'
data = pd.read_csv(url)

for i in range (len(data)):
    if data.species_group[i] == "Angelica":
        print(data.id_species[i],data.Images[i],i)