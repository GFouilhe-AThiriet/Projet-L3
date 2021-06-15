import os
import csv
import pandas as pd
import numpy as np

# Transform class_names into class_names_2

#Dataframe with id_species, species_name
data = pd.read_csv(os.path.join('C:','\\Users','lyz50',"documents","Github","Projet-L3","class_names.csv"))

species_name = data.species_name.to_numpy()

L=[]
for i in range (len(data)):
    species_group=""
    j=0
    while species_name[i][j]!="_":
        species_group=species_group+species_name[i][j]
        j=j+1
    L+=[species_group]

group = pd.Series(L)

# a=[]
# for i in range(len(L)):
#     switch=0
#     for j in range(len(a)):
#         if a[j]==L[i]:
#                 switch=1
#     if switch==0:
#         a+=[L[i]]

data.insert(2, "genus", group)
data.to_csv("class_names_2",index=False)