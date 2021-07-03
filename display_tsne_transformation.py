# Display the tsne transformation

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

from functions import *

def tsne_transformation(data,dim,path_to_train):

    global switch
    switch = 0
    global coord
    coord = "not initialised"
    global species_index
    species_index = "not selected"
    global error
    error = 0
    global a
    a = ""
    global b
    b = ""
    global c
    c = ""

    if dim == 3:
        
        x = data._3D_tsne_1
        y = data._3D_tsne_2
        z = data._3D_tsne_3
        label = data.id_species

        fig = plt.figure(figsize=(14,6))
        fig.suptitle('TSNE transformation of '+str(len(data))+" vectors")

        def on_click(event):
            xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
            global coord
            coord = ax1.format_coord(xmouse, ymouse)
            # print("Coordinates : ",coord)
            global switch
            switch = 1
            #print("on_click")
            global species_index
            global error
            global a
            global b
            global c
            a, b, c, species_index , error = decipher_coord(coord,data,3)
            if error != "too big":
                error = round(error,2)

        def animate(i):
            global switch
            if switch == 1: # If the user has clicked
                ax2.clear()
                ax2.axis("off")

                ax1.set_title(
                    coord +
                     " read "+
                     a +
                     "," +
                     b +
                     "," +
                     c +
                     " ; Cursor error = " +
                      str(error)
                      )

                if error != "too big":
                    ax2.set_title(
                        data.species_name[species_index] +
                        " / "+
                        str(data.id_species[species_index])
                    )

                    DIR = str(data.id_species[species_index])
                    path_to_DIR = os.path.join(path_to_train,DIR)
                    os.chdir(path_to_DIR)
                    if os.listdir() != 0:
                        image = os.listdir()[0]
                        read_image = plt.imread(os.path.join(path_to_DIR,image))
                        plt.imshow(read_image)
                    else:
                        ax2.set_title("No images; empty species folder")

                #print("animate")
                switch = 0

        ax1 = fig.add_subplot(1,2,1,projection ='3d')
        scatter = ax1.scatter(x, y, z,c=label,picker = True)
        ax1.set_xlabel("tsne_1")
        ax1.set_ylabel("tsne_2")
        ax1.set_zlabel("tsne_3")
        ax1.set_title(coord)
        
        legend = ax1.legend(
            *scatter.legend_elements(num=10),
            bbox_to_anchor=(-0.3,1),
            loc=2,
            title="Class")

        ax1.add_artist(legend)

        ax2 = fig.add_subplot(1,2,2)
        ax2.axis("off")

        fig.canvas.callbacks.connect('pick_event', on_click)

        anim = FuncAnimation(fig, animate, frames=100,interval=1000)
        # After (too) many hours of bugs, I think that a big value for interval might be necessary.

        plt.show()

    if dim == 2:
        
        x = data._2D_tsne_1
        y = data._2D_tsne_2
        label = data.id_species

        fig = plt.figure(figsize=(14,6))
        fig.suptitle('TSNE transformation of '+str(len(data))+" vectors")

        def on_click(event):
            xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
            global coord
            coord = ax1.format_coord(xmouse, ymouse)
            # print("Coordinates : ",coord)
            global switch
            switch = 1
            #print("on_click")
            global species_index
            global error
            global a
            global b
            global c
            a, b, c, species_index , error = decipher_coord(coord,data,2)
            if error != "too big":
                error = round(error,2)

        def animate(i):
            global switch
            if switch == 1: # If the user has clicked
                ax2.clear()
                ax2.axis("off")

                ax1.set_title(
                    coord +
                     " read "+
                     a +
                     "," +
                     b +
                     " ; Cursor error = " +
                      str(error)
                      )

                if error != "too big":
                    ax2.set_title(
                        data.species_name[species_index] +
                        " / "+
                        str(data.id_species[species_index])
                    )

                    DIR = str(data.id_species[species_index])
                    path_to_DIR = os.path.join(path_to_train,DIR)
                    os.chdir(path_to_DIR)
                    if os.listdir() != 0:
                        image = os.listdir()[0]
                        read_image = plt.imread(os.path.join(path_to_DIR,image))
                        plt.imshow(read_image)
                    else:
                        ax2.set_title("No images; empty species folder")

                #print("animate")
                switch = 0

        ax1 = fig.add_subplot(1,2,1)
        scatter = ax1.scatter(x, y ,c=label,picker = True)
        ax1.set_xlabel("tsne_1")
        ax1.set_ylabel("tsne_2")
        ax1.set_title(coord)
        
        legend = ax1.legend(
            *scatter.legend_elements(num=10),
            bbox_to_anchor=(-0.3,1),
            loc=2,
            title="Class")

        ax1.add_artist(legend)

        ax2 = fig.add_subplot(1,2,2)
        ax2.axis("off")

        fig.canvas.callbacks.connect('pick_event', on_click)

        anim = FuncAnimation(fig, animate, frames=100,interval=1000)
        # After (too) many hours of bugs, I think that a big value for interval might be necessary.

        plt.show()

