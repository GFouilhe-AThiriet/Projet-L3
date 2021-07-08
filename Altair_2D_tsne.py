import os
import csv
import pandas as pd
import altair as alt # You might need to install it
import altair_viewer # You might need to install it

from functions import *

alt.renderers.enable('altair_viewer')

# Dataframe

def altair_2D_tsne_chart(data):

    scales = alt.selection_interval(bind='scales')

    chart = alt.Chart(data.reset_index(),title="2D TSNE of the images embeddings").mark_point().encode(
        x ="_2D_tsne_1",
        y ="_2D_tsne_2",
        color = alt.Color('id_species', scale=alt.Scale(scheme='viridis'))
    ).encode(
        tooltip=['_2D_tsne_1','_2D_tsne_2','id_species','species_name']
        ).add_selection(
        scales
    )

    chart.encoding.x.title = 'tsne_1'
    chart.encoding.y.title = 'tsne_2'

    chart.show()
