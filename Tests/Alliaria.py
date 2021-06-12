import os
import pandas as pd

url = 'https://raw.githubusercontent.com/GFouilhe-AThiriet/Projet-L3/main/Miscellaneous/groups.csv'
data = pd.read_csv(url)

for i in range (len(data)):
    if data.species_group[i] == "Alliaria":
        print(data.id_species[i],data.species_name[i],data.Images[i])

# un doublon également pour le metasequoia ?