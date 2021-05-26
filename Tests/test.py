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

print(int(0.1))