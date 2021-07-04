# Waiting for the embeddings,
# we'll use a commun dataset of sklearn for the TSNE columns

# We will create to columns, one for a 2D-TSNE and one for a 3D-TSNE

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import csv

from functions import *

User = "Aurélien"
path_to_train , path_to_folder = user_paths(User)

data = pd.read_csv(os.path.join(path_to_folder,"class_names_2.csv"))
data.sort_values(by=["id_species"], inplace=True, ascending=True)

A_size_0 = len(data)
A_size_1 = 100

A = np.zeros((A_size_0,A_size_1))
for i in range (A_size_0):
    A[i] = i*np.ones(A_size_1)

label = list(i for i in range(len(data)))

# 2D TSNE transformation

n_components = 2

tsne = TSNE(n_components)
tsne_result = tsne.fit_transform(A)

# print(tsne_result.shape)
# print(tsne_result)

data.insert(5, "_2D_tsne_1", tsne_result[:,0])
data.insert(6, "_2D_tsne_2", tsne_result[:,1])

# 3D TSNE transformation

n_components = 3

tsne = TSNE(n_components)
tsne_result = tsne.fit_transform(A)

data.insert(7, "_3D_tsne_1", tsne_result[:,0])
data.insert(8, "_3D_tsne_2", tsne_result[:,1])
data.insert(9, "_3D_tsne_3", tsne_result[:,2])

# print(tsne_result.shape)
# print(tsne_result)

data.to_csv("class_names_2.csv",index=False)
