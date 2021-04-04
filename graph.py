##Librairies

import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

##Notes

#To comment a section on VSC : ctr+K then ctr+C ; ctr+k then ctr+U to uncomment
# ctr+alt+n shortcut to run the code
# double the \ to make os.chdir works
# for instance : C:\Users\lyz50\desktop should be :
#  os.chdir('C:\\Users\\lyz50\\documents') ; then it works

##Documentation
# https://www.youtube.com/watch?v=tJxcKyFMTGo for os

path_to_train='C:\\Users\\lyz50\\Documents\\GitHub\\plantnet_dataset\\python\\train'

os.chdir(path_to_train)

x,y=np.zeros(len(os.listdir())),np.zeros(len(os.listdir()))

i=0
for DIR in os.listdir():
    x[i]=DIR
    dir_path=path_to_train+'\\'+DIR
    y[i] = len([name for name in os.listdir(DIR)])
    i+=1

new_x,new_y=[],[]
for i in range (len(x)):
    if y[i]!=0:#delete the value y[i]=0 for a prettier graph
        new_x+=[x[i]]
        new_y+=[y[i]]


df = pd.DataFrame({"Species":new_x,"Images":new_y})
df = df.sort_values("Images",ascending=False)
df = df.reset_index(drop=True)
#print(df)

#Section (*) To get a standard graph
array=df.to_numpy()#array=([new_x_i,new_y_i]) and new_y is in sorted in descending order in df
new_y_ordered=[]
for i in range (len(array)):
    new_y_ordered+=[array[i][1]]
#End of Section (*)

bar_width=0.8

plt.clf()
plt.bar(df.index,"Images",data=df,width=bar_width)
plt.xlabel("Species",size="15")
plt.ylabel("Number of Images",size="15")
plt.title("Number of images for each species")
plt.show()

plt.clf()
plt.plot(df.index,new_y_ordered,"o",color="red")
plt.xlabel("Species",size="15")
plt.ylabel("Number of Images",size="15")
plt.title("Number of images for each species")
plt.show()
