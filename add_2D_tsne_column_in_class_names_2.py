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

# for n_components in range(2,2): # n_components = 2 and then n_components = 3

#     label = list(i for i in range(A_size_0))

#     # TSNE

#     tsne = TSNE(n_components)
#     tsne_result = tsne.fit_transform(A)

#     # print(tsne_result.shape)
#     # print(tsne_result)

#     tsne_result_data = pd.DataFrame(
#         {'tsne_1': tsne_result[:,0],
#         'tsne_2': tsne_result[:,1],
#         'tsne_3': tsne_result[:,2],
#         'label': label
#         })

#     print(tsne_result_data)

#     # tsne_result_data.to_csv("tsne_result_data_for_"+str(A_size_0)+"_vectors.csv",index=False)
