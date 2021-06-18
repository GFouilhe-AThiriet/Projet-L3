# Projet-L3

### Introduction

We are two 3rd year students in Mathematics at the University of Montpellier. We are taking part in a research project under supervision of Joseph Salmon, Benjamin Charlier and Camille Garcin.
It mainly focuses on various visualisation tasks of a sample of a Pl@ntNet dataset.

### Dataset

https://gitlab.inria.fr/cgarcin/plantnet_dataset

### Fill the parameters to run the code

1. Download this github repertory
2. Install Pygame (pip install Pygame)
3. In functions.py, complete path_to_train and path_to_folder leading respectively to the dataset train and to our downloaded github
4. Complete your name in Pl@ntNet_main_menu_window.py
5. To update class_names.csv if necessary : replace class_names.csv by the new csv file and then name it class_names.csv. Delete class_names_2.csv and then run create_class_names_2.py.

NB : Two people downloading the dataset Train might end up with two slightly different dataset as 0.1% of the images might be discarded during the download of the plants' pictures. If have updated class_names.csv, you might also need to update the graph of the Pareto effect.
In any case, if you want to have the exact graph of the Pareto effect corresponding to the exact dataset in your computer, follow the follow steps.

1. Delete class_names_2.csv
2. Run create_class_names_2.py; thus the number of images for each species in class_names_2.csv will absolutely fit the dataset in your computer
3. Run graph.py and save the picture of the graph in Pygames_elements as images_for_each_species.png, replacing the precedent picture
4. In Pl@ntNet_main_menu_window.py, adapt the position of the image by adapting the x and y coordinates of the picture : screen.blit(images_repartition,(0.01*w,0.15*h)). Then adapt the a and b values corresponding to the rims of the graph in order that the cursor position fits the displayed legend : a , b = 0.085 , 0.585. (Uncomment #draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")",medium_font, black, screen, 0.8*w,0) to see the position of the cursor in real time).
