import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from matplotlib.animation import FuncAnimation
import csv

# second_sub_plot=fig.add_subplot(1, 2, 2)#position of the subplot
# subplot_title=("Subplot0")
# second_sub_plot.set_title(subplot_title)  
# plt.axis('off')
# plt.imshow(read_image)
# plt.show()

# #To get the coordinates of the mouse in real time
# coords=[[0,0]] #Global Variable

# def onclick(event):
#     x,y=event.xdata, event.ydata
#     global coords
#     coords+=[[int(x),int(y)]]
#     print(coords)

A_size_0 = 200
A_size_1 = 100
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

x = tsne_result_data['tsne_1']
y = tsne_result_data['tsne_2']
z = tsne_result_data['tsne_3']

fig = plt.figure(figsize=(14,6))
fig.suptitle('TSNE transformation of '+str(A_size_0)+" vectors")

ax1 = fig.add_subplot(1,2,1,projection ='3d')
scatter = ax1.scatter(x, y, z,c=label)
ax1.set_xlabel("tsne_1")
ax1.set_ylabel("tsne_2")
ax1.set_zlabel("tsne_3")

legend = ax1.legend(
    *scatter.legend_elements(num=10),
    bbox_to_anchor=(-0.3,1),
    loc=2,
    title="Class")

ax1.add_artist(legend)

ax2 = fig.add_subplot(1,2,2)
ax2.axis("off")

# fig.canvas.mpl_connect('button_press_event', onclick)

def animate(i):
    ax2.clear()
    ax2.axis("off")
    fig.suptitle('TSNE transformation of '+str(A_size_0)+" vectors"+str(i))
    ax2.plot([1,2,3], [np.sin(i),np.cos(i),np.tan(i)],"o")
#     number_y=int(array[number][2])
#     subplot_title=("Species+ n°"+str(number))
#     second_sub_plot.set_title(subplot_title)
#     DIR=array[number][0]
#     path_to_DIR = os.path.join(path_to_train,DIR)#to change the plant picture
#     os.chdir(path_to_DIR)
#     image=os.listdir()[plant_representative]
#     read_image=plt.imread( os.path.join(path_to_DIR,image))
#     plt.imshow(read_image)

anim = FuncAnimation(fig, animate, frames=10,interval=1000)
# After (too) many hours of bugs, I think that a big value for interval might be necessary.

plt.show()
