# Display the tsne transformation

from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import numpy as np

from functions import *

def tsne_transformation(data,dim):

    if dim == 3:
        
        x = data._3D_tsne_1
        y = data._3D_tsne_2
        z = data._3D_tsne_3
        label = data.id_species

        fig = plt.figure(figsize=(14,6))
        fig.suptitle('TSNE transformation of '+str(len(data))+" vectors")

        global switch
        switch = 0
        global coord
        coord = "not initialised"
        global species_index
        species_index = 0

        def on_click(event):
            # artist = event.artist
            # print ('Object picked:', artist)
            xmouse, ymouse = event.mouseevent.xdata, event.mouseevent.ydata
            global coord
            coord = ax1.format_coord(xmouse, ymouse)
            if coord != "not initialised":
                global species_index
                species_index = decipher_coord(coord,data,3)
                print(species_index)
            # print("Coordinates : ",coord)
            # print ("Selection", ind)
            global switch
            switch = 1
            #print("on_click")

        def animate(i):
            global switch
            if switch == 1: #If the user has clicked
                ax2.clear()
                ax2.axis("off")
                ax1.set_title(coord)
                ax2.set_title(species_index)
                ax2.plot([1,2,3], [np.sin(i),np.cos(i),np.tan(i)],"o")
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

        ####

        #     number_y=int(array[number][2])
        #     subplot_title=("Species+ n°"+str(number))
        #     second_sub_plot.set_title(subplot_title)
        #     DIR=array[number][0]
        #     path_to_DIR = os.path.join(path_to_train,DIR)#to change the plant picture
        #     os.chdir(path_to_DIR)
        #     image=os.listdir()[plant_representative]
        #     read_image=plt.imread( os.path.join(path_to_DIR,image))
        #     plt.imshow(read_image)

        fig.canvas.callbacks.connect('pick_event', on_click)

        anim = FuncAnimation(fig, animate, frames=100,interval=1000)
        # After (too) many hours of bugs, I think that a big value for interval might be necessary.

        plt.show()


# second_sub_plot=fig.add_subplot(1, 2, 2)#position of the subplot
# subplot_title=("Subplot0")
# second_sub_plot.set_title(subplot_title)  
# plt.axis('off')
# plt.imshow(read_image)
# plt.show()