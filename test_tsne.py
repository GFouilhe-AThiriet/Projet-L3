import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

global L
L =[]

def on_pick(event):
    artist = event.artist
    xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
    coord = ax.format_coord(xmouse, ymouse)
    global L
    L += [[coord]]
    ind = event.ind
    ind = ind[0]
    print ('Object picked:', artist)
    print ("Selection", ind)
    print("Coordinates : ",coord)
    
def display_function(A_size_0=200,A_size_1=100):
    
    n_components = 3

    A = np.zeros((A_size_0,A_size_1))
    for i in range (A_size_0):
        A[i] = i*np.ones(A_size_1)

    print("A")
    print(A)

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

    print(tsne_result_data)

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

    fig.canvas.callbacks.connect('pick_event', on_pick)
    plt.title(str(A_size_0)+"_vectors")
    plt.show()

display_function(200,100)