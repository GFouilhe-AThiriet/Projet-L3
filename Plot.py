import os, os.path
import numpy as np
import matplotlib.pyplot as plt

os.chdir('C:\\Github\\plantnet_dataset\\plantnet_subset')
x = np.zeros(len(os.listdir()))
y = np.zeros(len(os.listdir()))

i = 0
for species in os.listdir():
    DIR = 'C:\\Github\\plantnet_dataset\\plantnet_subset\\' + str(species)
    y[i] = len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
    x[i] = species
    i +=1
    # print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))

plt.plot(np.array(x),np.array(y))
#print(x)
#print(y)
len(os.listdir())