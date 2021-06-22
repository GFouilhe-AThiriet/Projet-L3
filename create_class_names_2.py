import os
import csv
import pandas as pd
import numpy as np

from functions import *

User = "Aurélien"
path_to_train , path_to_folder = user_paths(User)

############# Transform class_names into class_names_2 #############

# Dataframe with id_species, species_name

data = pd.read_csv(os.path.join(path_to_folder,"class_names.csv"))

species_name = data.species_name

# Genus

L = []
for i in range (len(data)):
    l = len(species_name[i])
    species_group = ""
    short_name = ""
    j=0
    while species_name[i][j]!=" ": # A space
        species_group += species_name[i][j]
        j=j+1
    L+=[species_group]

    # To only have : "Loropetalum chinense" instead of "Loropetalum chinense (R. Br.) Oliv."

    if l>j+1:

        j=j+1

        # Sometimes there is a "x" : 1419115,Pelargonium x hortorum L.H. Bailey
        if species_name[i][j]=="x" or species_name[i][j]=="X":
            j=j+1
            if species_name[i][j]==" ":
                j=j+1
            else:
                j=j-1
        #

        while species_name[i][j]!=" " and j<l-1: # A space
            short_name += species_name[i][j]
            j=j+1
        data.species_name[i] = short_name

    # End of To only have : "Loropetalum chinense" instead of "Loropetalum chinense (R. Br.) Oliv."


group = pd.Series(L)

data.insert(2, "genus", group)

# Number of images of each species

Images = []
for i in range(len(data)):
    id_species = data.id_species[i]
    path_to_DIR = os.path.join(path_to_train,str(id_species))
    os.chdir(path_to_DIR)
    Images += [len(os.listdir())]

os.chdir(path_to_folder)
data.insert(3, "Images", Images)
data.sort_values(by=['Images'], inplace=True, ascending=False)
data.reset_index(drop=True,inplace=True) # Re-index

# Let's obtain the number of images per genus (for the other order of the scrolling list)

list_of_groups = make_a_list_of_groups(data.genus)

L=np.zeros(len(list_of_groups),dtype=int)

for genus_index in range (len(list_of_groups)):
    a=0
    for k in range(len(data)):
        if data.genus[k] == list_of_groups[genus_index] :
            L[genus_index]+= data.Images[k]

H=[]
for i in range (len(data)):
    for genus_index in range (len(list_of_groups)):
        if data.genus[i] == list_of_groups[genus_index]:
            H+=[L[genus_index]]

data.insert(4, "genus_images", H)
# End of Nmber of images per genus (for the other order of the scrolling list)

data.to_csv("class_names_2.csv",index=False)

