import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

path_to_save_figures = os.path.join('C:','\\Users','lyz50',"documents","tsne_images")
os.chdir(path_to_save_figures)

def display_function(A_size_0=200,A_size_1=100):
    
    n_components = 3

    A = np.zeros((A_size_0,A_size_1))
    for i in range (A_size_0):
        A[i] = i*np.ones(A_size_1)

    # Label

    label = list(i for i in range(A_size_0))

    # TSNE

    tsne = TSNE(n_components)
    tsne_result = tsne.fit_transform(A)

    # print(tsne_result.shape)
    # print(tsne_result)

    tsne_result_data = pd.DataFrame(
        {'tsne_1': tsne_result[:,0],
        'tsne_2': tsne_result[:,1],
        'tsne_3': tsne_result[:,2],
        'label': label
        })

    # 3D Display - Test 1
    fig = plt.figure(figsize=(8, 5))
    global ax
    ax = fig.add_subplot(projection ='3d')

    x = tsne_result_data['tsne_1']
    y = tsne_result_data['tsne_2']
    z = tsne_result_data['tsne_3']

    ax.set_xlabel("tsne_1")
    ax.set_ylabel("tsne_2")
    ax.set_zlabel("tsne_3")

    scatter = ax.scatter(x, y, z,c=label,picker = True)

    legend = ax.legend(
        *scatter.legend_elements(num=10),
        bbox_to_anchor=(1.2,1),
        loc=2,
        title="Class")

    ax.add_artist(legend)
    plt.title(str(A_size_0)+"_vectors")
    fig.savefig(os.path.join(path_to_save_figures,str(A_size_0)+"_vectors.png"))

#####################################################################################

L = np.linspace(1000,20000,20,dtype=int)

for i in range(len(L)):
    display_function(L[i],100)
    print(str(L[i])+"_vectors.png saved")