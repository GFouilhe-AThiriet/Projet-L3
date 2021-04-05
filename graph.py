# %%
##Librairies

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

##Notes

#To comment a section on VSC : ctr+K then ctr+C ; ctr+K then ctr+U to uncomment
# ctr+alt+n shortcut to run the code
# double the \ to make os.chdir works
# for instance : C:\Users\lyz50\desktop should be :
#  os.chdir('C:\\Users\\lyz50\\documents') ; then it works

##Documentation
# https://www.youtube.com/watch?v=tJxcKyFMTGo for os

student1 = False #Aurélien 
student2 = True  #Guilhem 
if student1:
    path_to_train = os.path.join('C:','Users','lyz50','Documents','GitHub','plantnet_dataset','python','train')
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

#Section (*) To get a standard graph
array = df.to_numpy()  # array=([new_x_i,new_y_i]) and new_y is in sorted in descending order in df
new_y_ordered = []
for i in range(len(array)):
    new_y_ordered += [array[i][1]]
#End of Section (*)

bar_width = 0.8

plt.clf()
plt.bar(df.index, "Images", data=df, width=bar_width)
plt.xlabel("Species")
plt.ylabel("Number of Images")
plt.title("Number of images for each species")
plt.show()

plt.clf()
plt.loglog(df.index, new_y_ordered / df["Images"].sum(),
           "o", color="red", ms=3,
           label="Plantnet distribution")
plt.xlabel("Species")
plt.ylabel("Number of Images")
plt.axhline(y=1/len(df.index), linestyle="--", label="Uniform distribution")
plt.title("Number of images for each species")
plt.legend()
plt.show()

# %%
