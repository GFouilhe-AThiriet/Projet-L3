##Librairies

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.widgets import Cursor, Button
from matplotlib.animation import FuncAnimation

##Notes

#To comment a section on VSC : ctr+K then ctr+C ; ctr+K then ctr+U to uncomment
# ctr+alt+n shortcut to run the code
# double the \ to make os.chdir works
# for instance : C:\Users\lyz50\desktop should be :
#  os.chdir('C:\\Users\\lyz50\\documents') ; then it works

# Next step : get the coordinates of the mouse in real time
# https://matplotlib.org/stable/users/event_handling.html maybe ?


##Documentation
# https://www.youtube.com/watch?v=tJxcKyFMTGo for os
# https://www.delftstack.com/fr/howto/matplotlib/add-subplot-to-a-figure-matplotlib/ for subplots
# https://brushingupscience.com/2016/06/21/matplotlib-animations-the-easy-way/ for matplotlib.animation.FuncAnimation

# https://realpython.com/python-matplotlib-guide/ for ax.plot instead of plt.plot
# https://stackoverflow.com/questions/43482191/matplotlib-axes-plot-vs-pyplot-plot for ax.plot (cf 1st comment)
# https://python4astronomers.github.io/plotting/advanced.html for ax.plot

# https://www.youtube.com/watch?v=YobjoBrND4w for mouse's coordinates

student1 = True #Aurélien 
student2 = False #Guilhem 
if student1:
    path_to_train = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset','python','train')
elif student2:
    path_to_train = os.path.join('C:/','plantnet_subset')
else:
    path_to_train = os.path.join("/home/jsalmon/Documents/Datasets/train")

os.chdir(path_to_train)

x, y = np.zeros(len(os.listdir())), np.zeros(len(os.listdir()))

i = 0
for DIR in os.listdir():
    x[i] = DIR
    y[i] = len([name for name in os.listdir(DIR)])
    i += 1

new_x, new_y = [], []
for i in range(len(x)):
    if y[i] != 0:  # delete values y[i]=0 for prettier graphs
        new_x += [x[i]]
        new_y += [y[i]]

df = pd.DataFrame({"Species":new_x, "Images":new_y})
df = df.sort_values("Images", ascending=False)
df = df.reset_index(drop=True)
#print(df)

####Plot the graph and the image
DIR='1355868'
path_to_DIR = os.path.join(path_to_train,DIR)
os.chdir(path_to_DIR)

image=os.listdir()[5]
read_image=plt.imread( os.path.join(path_to_DIR,image))

fig=plt.figure()

#Bar plot

bar_width = 5

first_sub_fig=fig.add_subplot(1, 1, 1)#position of the subplot
subplot_title=("Number of images for each species")
first_sub_fig.set_title(subplot_title)
first_sub_fig.set_ylabel("Species")
first_sub_fig.set_ylabel("Number of Images")
first_sub_fig.bar(df.index, "Images", data=df, width=bar_width)

cursor = Cursor(first_sub_fig, color='red', linewidth=2)#vertical and horizontal lines

#Plant image
second_sub_plot=fig.add_subplot(1, 2, 2)#position of the subplot
subplot_title=("Subplot0")
second_sub_plot.set_title(subplot_title)  
plt.axis('off')
plt.imshow(read_image)

plt.show()

####End of 'Plot the graph and the image'

##Two Other Visualisations :

array = df.to_numpy()  # array=([new_x_i,new_y_i]) and new_y is in sorted in descending order in df
new_y_ordered = []
for i in range(len(array)):
    new_y_ordered += [array[i][1]]

#To get the coordinates of the mouse in real time
MOUSE=[[17,17]] #Global Variable
print(MOUSE)
print("Corretly printed")
def onclick(event):
    x,y=event.xdata, event.ydata
    print(x,y)
    #print(MOUSE)
    #MOUSE+=[[x,y]]
    #print("END OF ONLICK")
#The First

fig=plt.figure()
ax=fig.add_subplot(1, 1, 1)#position of the subplot
ax.plot(df.index, new_y_ordered,"o", color="red")
ax.set_xlabel("Species")
ax.set_ylabel("Number of Images")
ax.set_title("Number of images for each species")

cursor = Cursor(ax,color='lightblue', linewidth=2)#vertical and horizontal lines

second_sub_plot=fig.add_subplot(1, 2, 2)#position of the subplot
subplot_title=("Subplot0")
second_sub_plot.set_title(subplot_title)  
plt.axis('off')
plt.imshow(read_image)

fig.canvas.mpl_connect('button_press_event', onclick)

def animate(i):
    subplot_title=('Species ' + str(i)+'(test)')
    second_sub_plot.set_title(subplot_title)  
anim = FuncAnimation(fig, animate, interval=100, frames=10)

plt.draw()
plt.show()

#The Second

# plt.clf()
# plt.loglog(df.index, new_y_ordered / df["Images"].sum(),
#            "o", color="red", ms=3,
#            label="Plantnet distribution")
# plt.xlabel("Species")
# plt.ylabel("Number of Images")
# plt.axhline(y=1/len(df.index), linestyle="--", label="Uniform distribution")
# plt.title("Number of images for each species")
# plt.legend()
# plt.show()
