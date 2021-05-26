import os
import csv
import pandas as pd
import altair as alt
import altair_viewer

# To import altair : https://altair-viz.github.io/getting_started/installation.html

alt.renderers.enable('altair_viewer')

########-----Altair Documentation-----########
# https://altair-viz.github.io/
# https://altair-viz.github.io/user_guide/display_frontends.html#display-general
# https://www.youtube.com/watch?v=x-iU2UwgVf0
# https://pypi.org/project/altair-viewer/
# https://towardsdatascience.com/python-interactive-data-visualization-with-altair-b4c4664308f8
# https://altair-viz.github.io/user_guide/interactions.html
# https://vegawidget.github.io/altair/articles/example-gallery-08-interactive-charts.html
# https://pypi.org/project/altair-images/
# https://matthewkudija.com/blog/2018/06/22/altair-interactive/
# https://altair-viz.github.io/user_guide/marks.html

User = "Aurélien"

if User=="Aurélien":
    path_to_train = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset','python','train')
    path_to_classnames = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset')
elif User=="Guilhem":
    path_to_train = os.path.join('C:/','Plantnet_project','plantnet_subset')
    path_to_classnames = os.path.join('C:/','Plantnet_project')
elif User=="Joseph":
    path_to_train = os.path.join("/home","jsalmon","Documents","Datasets","train")
    path_to_classnames = os.path.join("/home","jsalmon","Documents","...")
elif User=="Camille":
    path_to_train = os.path.join("...")
    path_to_classnames = os.path.join("...")

#Dataframe with index, id_species, species_name, Images (number of images) sorted by decreasing number of images 
url = 'https://raw.githubusercontent.com/GFouilhe-AThiriet/Projet-L3/main/data.csv'
data = pd.read_csv(url)

print(data)

chart = alt.Chart(data,title="Number of Images for each species in the Dataset").mark_point().encode(
    x="index",
    y="Images"
).encode(tooltip=['species_name','Images'])

chart.encoding.x.title = 'Species'
chart.encoding.y.title = 'Images'

chart.show()

