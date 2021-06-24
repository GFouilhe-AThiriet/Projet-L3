import os
import pandas as pd

from functions import *

User = "Aurélien"
path_to_train , path_to_folder = user_paths(User)

############# Transform class_names into class_names_2 #############

# Dataframe with id_species, species_name

data = pd.read_csv(os.path.join(path_to_folder,"class_names_2.csv"))

for i in range (len(data)):
    if data.genus[i] == "Alliaria":
        print(data.id_species[i],data.species_name[i],data.Images[i])

# un doublon également pour le metasequoia