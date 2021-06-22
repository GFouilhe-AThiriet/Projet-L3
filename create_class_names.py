import json
import csv
import pandas as pd
import numpy as np

from functions import *

User = "Aurélien"
path_to_train , path_to_folder = user_paths(User)

############# Transform data.json into class_names.csv #############

path_to_file = os.path.join(path_to_folder,"data.json")

data = pd.read_json(path_to_file,typ='columns')

data.to_csv("class_names.csv")

# Then name the columns (manually) : id_species, species_name

# NB :
# data = data.rename(columns = {'id_species':'species_name'}, inplace = True)
# doesn't work because : "AttributeError: 'Series' object has no attribute 'columns'"
# I haven't found how to fix that

