import os
import csv
import matplotlib.pyplot as plt
import pandas as pd
import altair as alt
import altair_viewer

# To import altair : https://altair-viz.github.io/getting_started/installation.html

########-----Altair Documentation-----########
# https://altair-viz.github.io/
# https://altair-viz.github.io/user_guide/display_frontends.html#display-general
# https://www.youtube.com/watch?v=x-iU2UwgVf0
# https://pypi.org/project/altair-viewer/
# https://towardsdatascience.com/python-interactive-data-visualization-with-altair-b4c4664308f8
# https://altair-viz.github.io/user_guide/interactions.html
# https://vegawidget.github.io/altair/articles/example-gallery-08-interactive-charts.html

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

brush = alt.selection_interval()

chart = alt.Chart(data).mark_point().encode(
    x="index",
    y="Images",
    color=alt.condition(brush, 'Origin:N', alt.value('lightgray'))

).add_selection(
    brush
)


chart.encoding.x.title = 'Species'
chart.encoding.y.title = 'Number of Images in the Dataset'

chart.show()