# Source : https://stackoverflow.com/questions/22052532/matplotlib-python-clickable-points

import matplotlib.pyplot as plt
import numpy as np

def on_pick(event):
    artist = event.artist
    xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
    x, y = artist.get_xdata(), artist.get_ydata()
    ind = event.ind
    ind = ind[0]
    print ('Object picked:', event.artist,"Selection",ind)
    print ('x, y of mouse:'.format(xmouse, ymouse))
    print ('Data point:', round(x[ind],3), round(y[ind],3))
    print ("")

fig, ax = plt.subplots()

ax.plot([5,6,7,8,9,10],np.exp([5,6,7,8,9,10]), 'ro-', picker = True)

fig.canvas.callbacks.connect('pick_event', on_pick)

plt.show()