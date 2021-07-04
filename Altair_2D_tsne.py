import os
import csv
import pandas as pd
import altair as alt
import altair_viewer

# To import altair : https://altair-viz.github.io/getting_started/installation.html

from functions import *

alt.renderers.enable('altair_viewer')

# Dataframe

def altair_2D_tsne_chart(data):

    scales = alt.selection_interval(bind='scales')

    chart = alt.Chart(data.reset_index(),title="2D TSNE of the images embeddings").mark_point().encode(
        x ="_2D_tsne_1",
        y ="_2D_tsne_2",
        color = 'id_species'
    ).encode(
        tooltip=['_2D_tsne_1','_2D_tsne_2','id_species','species_name']
        ).add_selection(
        scales
    )

    chart.encoding.x.title = 'tsne_1'
    chart.encoding.y.title = 'tsne_2'

    chart.show()
