import os
import csv
import pandas as pd
import numpy as np

from functions import *

# Transform class_names_2 into class_names_3

path_to_train , path_to_folder = user_paths("Aurélien")

#Dataframe with id_species, species_name
data = pd.read_csv(os.path.join('C:','\\Users','lyz50',"documents","Github","Projet-L3","class_names_2.csv"))

Images = []
for i in range(len(data)):
    id_species = data.id_species[i]
    path_to_DIR = os.path.join(path_to_train,str(id_species))
    os.chdir(path_to_DIR)
    Images += [len(os.listdir())]

os.chdir(path_to_folder)
data.insert(3, "Images", Images)
data.sort_values(by=['Images'], inplace=True, ascending=False)
data.to_csv("class_names_3",index=False)