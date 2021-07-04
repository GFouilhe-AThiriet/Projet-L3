import os
import csv
import pandas as pd
import altair as alt
import altair_viewer

# To import altair : https://altair-viz.github.io/getting_started/installation.html

from functions import *

User = "Aurélien"
path_to_train , path_to_folder = user_paths(User)

alt.renderers.enable('altair_viewer')

# Dataframe
data = pd.read_csv(os.path.join(path_to_folder,"class_names_2.csv"))

data.sort_values(by=["Images"], inplace=True, ascending=False)
# Sorted by decreasing order of number of images
data.reset_index(drop=True, inplace=True)
# Re-index

chart = alt.Chart(data.reset_index(),title="Number of Images for each species in the Dataset").mark_point().encode(
    x="index",
    y="Images"
).encode(
    tooltip=['id_species','species_name','Images']
    )

chart.encoding.x.title = 'Species'
chart.encoding.y.title = 'Images'

chart.show()
