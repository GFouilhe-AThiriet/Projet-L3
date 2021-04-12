#---Librairies-------------
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.widgets import Cursor, Button
from matplotlib.animation import FuncAnimation
import csv
#--------------------------

#---------Notes------------
    #To comment a section on VSC : ctr+K then ctr+C ; ctr+K then ctr+U to uncomment
    #ctr+alt+n shortcut to run the code
    #Remaining : a right click event to add +1 to plant_representative
        #and 0 if plant_representative=len(os.list(DIR))
        #in order to change the plant picture from a same species in the directory
#--------------------------

#-------User selection-----
student1 = False #Aurélien 
student2 = True  #Guilhem 
if student1:
    path_to_train = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset','python','train')
    path_to_classnames = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset')
elif student2:
    path_to_train = os.path.join('C:/','Plantnet_project','plantnet_subset')
    path_to_classnames = os.path.join('C:/','Plantnet_project')
else:
    path_to_train = os.path.join("/home/jsalmon/Documents/Datasets/train")
#--------------------------

#------Functions-----------

#---To get the coordinates of the mouse in real time--

def animate(i):
    number=coords[-1][0]
    if number<0 or number>len(np.array(df.id_species)):
        number=-1
        number_y=-1
    else:
        number_y = int(df.Images[number]) 
        subplot_title='n°'+str(number) + ' '+ str(df.species_name[number])
    if number>0:
        second_sub_plot.set_title(subplot_title)
        DIR= str(df.id_species[number])    
        path_to_DIR = os.path.join(path_to_train,DIR)#to change the plant picture
        os.chdir(path_to_DIR)
        image=os.listdir()[plant_representative]
        read_image=plt.imread(os.path.join(path_to_DIR,image))
        plt.imshow(read_image)

coords=[[0,0]] #Global Variable

def onclick(event):
    x,y=event.xdata, event.ydata
    global coords
    coords+=[[int(x),int(y)]]

#Dataframe with id_species, species_name, Images (number of images) sorted by decreasing number of images 
url = 'https://raw.githubusercontent.com/GFouilhe-AThiriet/Projet-L3/main/data.csv'
df = pd.read_csv(url)

DIR='1357367' #Dir of initial picture on plot
path_to_DIR = os.path.join(path_to_train,DIR)
os.chdir(path_to_DIR)

plant_representative=0

image=os.listdir()[plant_representative]
read_image=plt.imread( os.path.join(path_to_DIR,image))


#---------------Plot the graph and the image-------------------------



# #---Bar plot : not animated yet------------------

# fig=plt.figure()
# bar_width = 5

# first_sub_fig=fig.add_subplot(1, 1, 1)#position of the subplot
# subplot_title=("Number of images for each species")
# first_sub_fig.set_title(subplot_title)
# first_sub_fig.set_ylabel("Species")
# first_sub_fig.set_ylabel("Number of Images")
# first_sub_fig.bar(df.index, "Images", data=df, width=bar_width)

# cursor = Cursor(first_sub_fig, color='red', horizOn=False, linewidth=2)#vertical line

# #--------Plant image ---------
# second_sub_plot=fig.add_subplot(1, 2, 2)#position of the subplot
# subplot_title=('')
# second_sub_plot.set_title(subplot_title)  
# plt.axis('off')
# plt.imshow(read_image)

# plt.show()


# #------------------------------------------------


#--Scatter plot (animation on)----------

fig=plt.figure(1)
ax=fig.add_subplot(1, 1, 1)#position of the subplot
ax.plot(df.index, df.Images,"o", color="red")
ax.set_xlabel("Species")
ax.set_ylabel("Number of Images")
ax.set_title("Number of images for each species")

cursor = Cursor(ax,color='lightblue', horizOn=False, linewidth=2)#vertical

second_sub_plot=fig.add_subplot(1, 2, 2)#position of the subplot
subplot_title=' '
second_sub_plot.set_title(subplot_title)  
plt.axis('off')
plt.imshow(read_image)

fig.canvas.mpl_connect('button_press_event', onclick)


anim = FuncAnimation(fig, animate, interval=100, frames=1)#change frames if it lags ??

plt.draw()
plt.show()

#-----loglog visualisation------

plt.figure(2)
plt.loglog(df.index, df.Images / df["Images"].sum(),
           "o", color="red", ms=3,
           label="Plantnet distribution")
plt.xlabel("Species")
plt.ylabel("Number of Images")
plt.axhline(y=1/len(df.index), linestyle="--", label="Uniform distribution")
plt.title("Number of images for each species")
plt.legend()
plt.show()
