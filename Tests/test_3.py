import os
import pandas as pd

url = 'https://raw.githubusercontent.com/GFouilhe-AThiriet/Projet-L3/main/Miscellaneous/groups.csv'
data = pd.read_csv(url)

n = 0

for i in range (len(data)):
    n += data.Images[i]

print("Number of images in the dataset : ",int(n))

# Aurélien : 306230
# Online : 306293