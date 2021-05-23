import os
import csv
import matplotlib.pyplot as plt
#import pandas as pd
#import altair as alt
#import altair_viewer

# # To import altair : https://altair-viz.github.io/getting_started/installation.html
# # You also have to install : altair_viewer

# # alt.renderers.enable('altair_viewer', inline=True)

# ########-----Altair Documentation-----########
# # https://altair-viz.github.io/
# # https://altair-viz.github.io/user_guide/display_frontends.html#display-general
# # https://www.youtube.com/watch?v=x-iU2UwgVf0
# # https://pypi.org/project/altair-viewer/

# # from vega_datasets import data
# # cars = data.cars()

# #chart = alt.Chart(cars).mark_point().encode(
# #    x='Horsepower',
# #    y='Miles_per_Gallon',
# #    color='Origin',
# #).interactive()

# #chart.show()

# url = 'https://raw.githubusercontent.com/GFouilhe-AThiriet/Projet-L3/main/data.csv'
# data = pd.read_csv(url)

# brush = alt.selection(type = "interval", encodings = list("x"))

# bars=alt.Chart().mark_bar().encode(
#     x = alt.X("date:O", timeUnit="month"),
#     y = "mean(precipitation):Q",
#     opacity = alt.condition(
#       brush, 
#       alt.OpacityValue(1), 
#       alt.OpacityValue(0.7)
#     )
#   ).properties(selection = brush)

# line=alt.Chart().mark_rule(color = "firebrick").encode(
#     y = "mean(precipitation):Q",
#     size = alt.SizeValue(3)
#   ).transform_filter(brush.ref())

# chart=alt.layer(bars, line, data = data)
# chart.show()

# # # from vega_datasets import data
# # # cars = data.cars()
# # # print(cars)