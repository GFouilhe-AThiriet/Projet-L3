##Librairies

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from matplotlib.widgets import Cursor, Button
from matplotlib.animation import FuncAnimation

import csv

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
# https://stackoverflow.com/questions/25521120/store-mouse-click-event-coordinates-with-matplotlib answer to the problem of 08/04

student1 = True #Aurélien 
student2 = False #Guilhem 
if student1:
    path_to_train = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset','python','train')
    path_to_classnames = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset')
elif student2:
    path_to_train = os.path.join('C:/','plantnet_subset')
else:
    path_to_train = os.path.join("/home/jsalmon/Documents/Datasets/train")

with open(path_to_classnames+"class_names.csv", mode ='r')as file:
    
  # reading the CSV file
  csvFile = csv.reader(file)
  
  # displaying the contents of the CSV file
  for lines in csvFile:
        print(lines)