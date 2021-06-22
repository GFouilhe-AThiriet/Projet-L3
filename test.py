# import plotly.graph_objects as go

# import pandas as pd
# import os
# import numpy as np

# student1 = False #Aurélien 
# student2 = True  #Guilhem 
# if student1:
#     path_to_train = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset','python','train')
#     path_to_classnames = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset')
# elif student2:
#     path_to_train = os.path.join('C:/','Plantnet_project','plantnet_subset')
#     path_to_classnames = os.path.join('C:/','Plantnet_project')
# else:
#     path_to_train = os.path.join("/home/jsalmon/Documents/Datasets/train")

# def animate(i):
#     number=coords[-1][0]
#     if number<0 or number>len(x):
#         number=-1
#         number_y=-1
#     else:
#         number_y = int(df.Images[number]) 
#         subplot_title='n°'+str(number) + ' '+ str(df.species_name[number])
#     if number>0:
#         second_sub_plot.set_title(subplot_title)
#         DIR= str(df.id_species[number])    
#         path_to_DIR = os.path.join(path_to_train,DIR)#to change the plant picture
#         os.chdir(path_to_DIR)
#         image=os.listdir()[plant_representative]
#         read_image=plt.imread( os.path.join(path_to_DIR,image))
#         plt.imshow(read_image)


# # load dataset

# #Dataframe from csv (df_names)
# path_csv=os.path.join(path_to_classnames,"class_names.csv")
# df_names = pd.read_csv(path_csv)
# df_names.columns = ['id_species', 'species_name'] #otherwise there is an ennoying space in ' species_name'
# #--------------------------

# #Dataframe with directories names and number of images (df)
# os.chdir(path_to_train)
# x, y = np.zeros(len(os.listdir())), np.zeros(len(os.listdir()))
# i = 0
# for DIR in os.listdir():
#     x[i] = DIR
#     y[i] = len([name for name in os.listdir(DIR)])
#     i += 1
# df = pd.DataFrame({"Directories":os.listdir(),"Species":x, "Images":y})

# #--------------------------

# #Merging dataframes then sort
# df = pd.concat([df_names.id_species,df_names.species_name, df.Images], axis = 1)
# df = df.sort_values("Images", ascending=False)
# df = df.reset_index(drop=True)

# # create figure
# fig = go.Figure()

# # Add surface trace
# fig.add_trace(go.Bar(y=df.Images))

# # # Update plot sizing
# # fig.update_layout(
# #     width=800,
# #     height=900,
# #     autosize=False,
# #     margin=dict(t=0, b=0, l=0, r=0),
# #     template="plotly_white",
# # )

# # # Update 3D scene options
# # fig.update_scenes(
# #     aspectratio=dict(x=1, y=1, z=0.7),
# #     aspectmode="manual"
# # )

# # # Add dropdown
# # fig.update_layout(
# #     updatemenus=[
# #         dict(
# #             type = "buttons",
# #             direction = "left",
# #             buttons=list([
# #                 dict(
# #                     args=["type", "surface"],
# #                     label="3D Surface",
# #                     method="restyle"
# #                 ),
# #                 dict(
# #                     args=["type", "heatmap"],
# #                     label="Heatmap",
# #                     method="restyle"
# #                 )
# #             ]),
# #             pad={"r": 10, "t": 10},
# #             showactive=True,
# #             x=0.11,
# #             xanchor="left",
# #             y=1.1,
# #             yanchor="top"
# #         ),
# #     ]
# # )

# # # Add annotation
# # fig.update_layout(
# #     annotations=[
# #         dict(text="Trace type:", showarrow=False,
# #                              x=0, y=1.08, yref="paper", align="left")
# #     ]
# # )

# fig.show()

# https://www.youtube.com/watch?v=0RryiSjpJn0
# https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame
# https://stackoverflow.com/questions/33296740/unboundlocalerror-local-variable-event-referenced-before-assignment-pygame
# https://stackoverflow.com/questions/34287938/how-to-distinguish-left-click-right-click-mouse-clicks-in-pygame
# Very interesting : https://www.reddit.com/r/pygame/comments/40873s/could_you_explain_for_event_in_pygameeventget/
# https://stackoverflow.com/questions/42215932/two-for-event-in-pygame-event-get
# https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame#:~:text=If%20the%20box%20is%20active,and%20reset%20it%20to%20%27%27%20.

# import pygame, sys
# import os
# import pandas as pd
# import numpy as np

# from functions import *

##################################################

################ Users' Parameters ###############

# # Complete the required paths in functions.py and then enter your name :

# User = "Aurélien"

# # If you don't have internet, write False and the species' data will
# # be read from the csv file instead of the online file

# internet = False

# ############ End of Users' Parameters ############

# ################## Global Setup ##################

# path_to_train, path_to_classnames, path_to_folder = user_paths(User)

# # Dataframe with index, id_species, species_name, Images (number of images)
# # sorted by decreasing number of images 

# if internet == True :
#     url = 'https://raw.githubusercontent.com/GFouilhe-AThiriet/Projet-L3/main/Miscellaneous/groups.csv'
#     data = pd.read_csv(url)
# else:
#     data = pd.read_csv(os.path.join(path_to_folder,"Miscellaneous","groups.csv")) 

# path_to_DIR = os.path.join(path_to_train,"1412445")
# print(path_to_DIR)
# os.chdir(path_to_DIR)
# print(os.listdir())

# import numpy as np
# print(np.zeros((2,4),dtype=int)[1][3])

import json
import pandas as pd
import os

from functions import *

User = "Aurélien"
path_to_train , path_to_folder = user_paths(User)

path_to_file = os.path.join(path_to_folder,"data.json")

data = pd.read_json(path_to_file,typ='series')
data.to_csv("class_names_2.csv",index=False)