import pygame, sys
import os
import pandas as pd
import numpy as np

from functions import *
from pygame.locals import *

##################################################

################ Users' Parameters ###############

# Note : you have to download the ENTIRE subset named "TRAIN" before lauching this code
# If you have only downloaded a sample of this subset, the code should not return errors
# but a standard image will be displayed instead of a missing species' photo.

# Complete the required paths in functions.py and then enter your name :

User = "Aurélien"

# If you don't have internet, write False and the species' data will
# be read from the csv file instead of the online file

internet = False

############ End of Users' Parameters ############


###################################################################################
###################################################################################

################## Global Setup ##################

path_to_train, path_to_classnames, path_to_folder = user_paths(User)

# Dataframe with index, id_species, species_name, Images (number of images)
# sorted by decreasing number of images 

if internet == True :
    url = 'https://raw.githubusercontent.com/GFouilhe-AThiriet/Projet-L3/main/Miscellaneous/groups.csv'
    data = pd.read_csv(url)
else:
    data = pd.read_csv(os.path.join(path_to_folder,"Miscellaneous","groups.csv")) 


list_of_groups = list_of_groups(data.species_group)
id_species_per_group = id_species_per_group(data.id_species,data.species_group,list_of_groups)

screen_width = 1400 # 1400 with 0.57 ratio might be a good size
ratio = 0.57

# NB : text font won't be affected by the size of the Window.
# Thus, you might have to change the global font manually below

mainClock = pygame.time.Clock()
pygame.init()

logo = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","Pl@ntNet_logo.png"))
logo = pygame.transform.scale(logo, (32,32))

pygame.display.set_icon(logo)
window_name = "Pl@ntNet"
pygame.display.set_caption(window_name)

r = ratio
screen_height = int(screen_width*r)

w , h = screen_width , screen_height

screen = pygame.display.set_mode((screen_width,screen_height))

############ End of Global Setup ############

############# Fonts and Colors ##############

mini_font = pygame.font.SysFont(None, 24)
medium_font = pygame.font.SysFont(None, 27)
big_font = pygame.font.SysFont(None, 50)

font = medium_font

white = (255,255,255)
black = (0,0,0)
grey = (96,119,117)
dark_grey = (64,64,64)
green = (0,200,0)
blue = (51,153,255)

button_color = white # Change it from white to blue to see margin's buttons

additional_color = white # Change it from white to green to see additional buttons

############# End of Fonts and Colors ##############

############ Pygales Elements ############

# Backgrounds :

list_of_backgrounds = []

for i in range(1,7):
    background = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","plantnet_background_"+str(i)+".jpg"))
    background_width , backgroundheight = background.get_rect().size
    background = pygame.transform.scale(background, (int((background_width*h)/backgroundheight),h))
    background_width , backgroundheight = background.get_rect().size
    list_of_backgrounds+=[background]

margin = w-background_width

# Arrows :

arrow_w = int(w*0.1)
arrow_h =  int(w*0.08)

arrow_back = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","arrow_back.png"))
arrow_back = pygame.transform.scale(arrow_back, (arrow_w, arrow_h))

arrow_back_grey = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","arrow_back_grey.png"))
arrow_back_grey = pygame.transform.scale(arrow_back_grey, (arrow_w,arrow_h))

right_arrow_size = int(arrow_w*0.6)

grey_right_arrow = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","grey_right_arrow.png"))
grey_right_arrow = pygame.transform.scale(grey_right_arrow, (right_arrow_size,right_arrow_size))

black_right_arrow = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","black_right_arrow.png"))
black_right_arrow = pygame.transform.scale(black_right_arrow, (right_arrow_size,right_arrow_size))

grey_left_arrow = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","grey_left_arrow.png"))
grey_left_arrow = pygame.transform.scale(grey_left_arrow, (right_arrow_size,right_arrow_size))

black_left_arrow = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","black_left_arrow.png"))
black_left_arrow = pygame.transform.scale(black_left_arrow, (right_arrow_size,right_arrow_size))

# Number of images for each species :

images_repartition = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","images_for_each_species.png"))
images_repartition_width , images_repartition_height = images_repartition.get_size()
coeff = images_repartition_height/images_repartition_width
images_repartition = pygame.transform.scale(images_repartition,(int(0.6*w),int(0.6*w*coeff)))

# Other :

wide_logo = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","Pl@ntNet_wide_logo.png"))
logo_width , logo_height = wide_logo.get_size()
coeff = logo_height/logo_width
wide_logo_1 = pygame.transform.scale(wide_logo, (int(0.3*w),int(w*0.3*coeff)))
wide_logo_2 = pygame.transform.scale(wide_logo, (int(0.5*w),int(w*0.5*coeff)))

no_images = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","Pl@ntNet_logo.png"))
no_images = pygame.transform.scale(no_images, (int(w*0.15),int(w*0.15)))

##############################################################################
################################################## Main part of the code below
##############################################################################

############ MENU ############

def menu():

    background_index = np.random.randint(0,6) # Initialisation

    while True:
        screen = pygame.display.set_mode((screen_width,screen_height))
        screen.fill(white)

        mx, my = pygame.mouse.get_pos()

        background_button = pygame.Rect(margin,0, background_width , backgroundheight)
        screen.blit(list_of_backgrounds[background_index],(margin,0))

        for event in pygame.event.get():
            if background_button.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    if background_index<5:
                        background_index+=1
                    else:
                        background_index=0
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        # draw_text("(x="+str(mx)+", y="+str(my)+")", font, black, screen, 0,0.6*h) 
        # draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")",
        # font, black, screen, 0,0.7*h)
        # Useful to see positions when placing things

        ####### Margin #######

        Images_button = pygame.Rect(0, h*0.1, margin, h*0.1)
        pygame.draw.rect(screen, button_color, Images_button)
        img_txt_position_x = w*0.01
        img_txt_position_y = h* 0.135

        if Images_button.collidepoint((mx, my)):
            draw_text('Number of images for each species', font, grey, screen, 
            img_txt_position_x, img_txt_position_y)
            if event.type == MOUSEBUTTONDOWN:
                Images()
        else:
            draw_text('Number of images for each species', font, black, screen,
            img_txt_position_x, img_txt_position_y)

        Groups_button = pygame.Rect(0, h*0.25,margin, h*0.1)
        pygame.draw.rect(screen, button_color, Groups_button)
        img_groups_position_x = w*0.1
        img_groups_position_y = h*0.29

        if Groups_button.collidepoint((mx, my)):
            draw_text('Groups', font, grey, screen,
            img_groups_position_x, img_groups_position_y)
            if event.type == MOUSEBUTTONDOWN:
                groups()
        else:
            draw_text('Groups', font, black, screen,
            img_groups_position_x, img_groups_position_y)

        ####### End of Margin #######
 
        pygame.display.update()
        mainClock.tick(60)


###################################################################################
###################################################################################

#### Number of images for each species ###

def Images():

    plant_representative = 0

    running = True

    a , b = 0.085 , 0.585
    # y position of the y axis and of the last species' data
    # on the x axis of the displayed graph

    while running:
        screen.fill(white)
        arrow_button = pygame.Rect(0.9*w,0, arrow_w, arrow_h)
        screen.blit(wide_logo_1,(0.345*w,h*0.00))

        screen.blit(images_repartition,(0.01*w,0.15*h)) # the graph

        mx, my = pygame.mouse.get_pos()
        
        # draw_text("(x="+str(mx)+", y="+str(my)+")", font, black, screen, 0.8*w,0.05*h)
        # draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")",
        # medium_font, black, screen, 0.8*w,0)
        # Useful to see positions when placing things

        # rect = pygame.Rect(0.65*w,0.23*h,int(w*0.3),int(w*0.3))
        # pygame.draw.rect(screen, green, rect)
        # In order to see the place where the plant image is displayed
        # Keep that uncomment please

        list_of_events = pygame.event.get()

        mxw = mx / w

        if a <= mxw and mxw <=b and my/h>0.23:

            abscisses = int((mxw-a)/(b-a)*1080)

            # draw_text("abscisses="+str(abscisses), medium_font, black, screen, 0.8*w,0.1*h)
            # Keep also that please

            if 0<=abscisses<=1080:
                species_name = data.species_name[abscisses]
                draw_text("Species : "+species_name, font, black, screen, 0.65*w,0.78*h)

                images = data.Images[abscisses]
                draw_text("Number of Images : "+str(images), font, black, screen, 0.65*w,0.81*h)

                id_species = data.id_species[abscisses]
                path_to_DIR = os.path.join(path_to_train,str(id_species))
                os.chdir(path_to_DIR)

                number_images = len(os.listdir()) # first part of gadget to change the plant photo whith right click
                if plant_representative > number_images-1:
                    plant_representative = 0

                if number_images>0: # Display of the photo of the plant-species
                    plant_image_jpg_name = os.listdir()[plant_representative]
                    plant_image = pygame.image.load(os.path.join(path_to_DIR,plant_image_jpg_name))
                    plant_image = pygame.transform.scale(plant_image, (int(w*0.3),int(w*0.3)))
                    screen.blit(plant_image,(0.65*w,0.23*h))

                for event in list_of_events: # second part of the gadget to change the plant representative with right click
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 3:
                            plant_representative += 1
        else:
                draw_text("Species : ", font, black, screen, 0.65*w,0.78*h)
                draw_text("Number of Images : ", font, black, screen, 0.65*w,0.81*h) 

        running = possibility_to_return_to_menu(list_of_events, running,screen,w,mx, my,
        arrow_button,arrow_back,arrow_back_grey)

        pygame.display.update()
        mainClock.tick(60)

#### End of Number of images for each species ###

###################################################################################
###################################################################################

#### GROUPS ###

def groups():

    j = 0
    actual_group = "not initialised"
    index_actual_group = 0
    interactive_text = "Click on a group name"
    list_of_species = []

    plant_representative = np.zeros((2,4),dtype=int)
    max_plant_representative = 5 # maximum value of plant_representative+1

    interval_w = 0.02
    interval_h = 0.05

    switch = 1 # When a new group is selected, switch takes 0 as a value and Pygame loads the images
    # of the selected group

    page = 1

    running = True

    while running :

        screen.fill(white)
        arrow_button = pygame.Rect(0.9*w,0, arrow_w, arrow_h)
        screen.blit(wide_logo_2,(0.25*w,0))

        mx, my = pygame.mouse.get_pos()
        
        # rect = pygame.Rect(0, h*0.06,margin, h*0.1)
        # pygame.draw.rect(screen, button_color, rect)
        # Keep that uncomment please

        # draw_text("(x="+str(mx)+", y="+str(my)+")", font, black, screen, 0.8*w,0.05*h)
        # draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")",
        # medium_font, black, screen, 0.8*w,0)
        # Useful to see positions when placing things

        list_of_events = pygame.event.get()

        ### Scrolling list ###

        for event in list_of_events:
            if event.type == KEYDOWN:
                if event.key == K_UP and j>0:
                    j+=-1
                if event.key == K_DOWN and j<len(list_of_groups)-40:
                    j+=1

            if mx<margin*0.6: 
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4 and j>0:
                        j+=-1
                    if event.button == 5 and j<len(list_of_groups)-40:
                        j+=1
                    if event.button == 1:

                        switch = 0 # in order that the loading of the images is only done once

                        page = 1

                        for i in range(40):
                            if my>h*(i+10)*0.02 and my<h*(i+11)*0.02:
                                actual_group = list_of_groups[i+j]
                                index_actual_group = i+j
                                list_of_species = []
                                for k in range(len(data)):
                                    if data.species_group[k] == actual_group :
                                        list_of_species += [data.species_name[k]]

           ### End of the Scrolling list ###

        ### Displayed Global Text ###
        
        # Title and Interactive research text (not active yet)

        draw_text('Groups', font, black, screen, w*0.09, 0.18*h)
        draw_text(interactive_text, font, black, screen, 0.04*w, h*0.1)

        draw_text("Group : "+actual_group+".", font, black, screen, margin, h*11*0.02)
        draw_text("Number of species : "+str(len(list_of_species)), font, black, screen,
        margin+(0.15+interval_w)*w, h*11*0.02)

        # for i in range(0,len(list_of_species)):
        #         draw_text(list_of_species[i], font, black, screen, w*0.5, h*i*0.02)
        # Let's keep that to control groups' species if necessary

        for i in range(1,40): # Display groups' names in the margin
            draw_text(list_of_groups[i+j], font, black, screen, 0, h*(i+10)*0.02)

        ### End of Displayed Global Text ###

        ############### SPECIES' NAMES AND PHOTOS IN A GROUP ###############
        
        more_button = pygame.Rect(0.92*w,0.7475*h, right_arrow_size, right_arrow_size)
        pygame.draw.rect(screen, additional_color, more_button)

        previous_button = pygame.Rect(0.165*w,0.7475*h, right_arrow_size, right_arrow_size)
        pygame.draw.rect(screen, additional_color, previous_button)

        ######################### Display species' photos and names #########################

        ### LOADING OF THE IMAGES FOR THE ACTUAL GROUP ###

        if switch == 0: # New group selected; Pygame has to load the images

            list_of_species_for_the_actual_group = id_species_per_group[index_actual_group]
            list_of_images_for_the_actual_group = []

            counter = 0

            for p in range(2):
                for i in range(4):
                    if (counter+(page-1)*8)<len(list_of_species):

                        rect = pygame.Rect(margin+i*(0.15+interval_w)*w, 0.27*h+p*(0.27+interval_h)*h, w*0.15, w*0.15 )
                        pygame.draw.rect(screen, green, rect)

                        path_to_DIR = os.path.join(path_to_train,str(list_of_species_for_the_actual_group[counter+(page-1)*8]))

                        os.chdir(path_to_DIR)

                        number_images = len(os.listdir()) # number of images for ONE species

                        if number_images > 0 :
                            list_of_images_of_the_same_species = []
                            for m in range(min(number_images,max_plant_representative)):
                                plant_image_jpg_name = os.listdir()[0]
                                plant_image = pygame.image.load(os.path.join(path_to_DIR,plant_image_jpg_name))
                                plant_image = pygame.transform.scale(plant_image, (int(w*0.15),int(w*0.15)))
                                list_of_images_of_the_same_species += [plant_image]
                            list_of_images_for_the_actual_group += [list_of_images_of_the_same_species]
                        else :
                            list_of_images_for_the_actual_group += [False] # No images for this species
                            
                        counter+=1

            switch = 1 # no need to load again the images for Pygame until another group is selected

        ### End of LOADING OF THE IMAGES FOR THE ACTUAL GROUP ###

        ####### Display of the images of this group #######

        counter = 0

        for p in range(2):
            for i in range(4):
                if (counter+(page-1)*8)<len(list_of_species):

                    # Display one images and names of each of the species of the group
                    if list_of_images_for_the_actual_group[counter] != False:
                        screen.blit(list_of_images_for_the_actual_group[counter][plant_representative[p][i]],
                        (margin+i*(0.15+interval_w)*w, 0.27*h+p*(0.27+interval_h)*h))
                    else:
                        screen.blit(no_images,
                        (margin+i*(0.15+interval_w)*w, 0.27*h+p*(0.27+interval_h)*h))
                    
                    draw_text(list_of_species[counter+(page-1)*8], font, black, screen,
                    margin+i*(0.15+interval_w)*w, 2*0.27*h+p*(0.27+interval_h)*h)

                    counter+=1

        ####### End of Display of the images of this group #######

        ### If there are more than 8 images to display ###

        if page > 1: # need to have the possibility to come back to the previous window
            for event in list_of_events:
                if previous_button.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        page+= -1
                        switch = 0 # have to load the images of the new page
            if previous_button.collidepoint((mx, my)):
                screen.blit(grey_left_arrow,(0.165*w,0.7475*h))
            else :
                screen.blit(black_left_arrow,(0.165*w,0.7475*h))

        if (len(list_of_species)-8*page)>=1: # then, need to have an additional window
            for event in list_of_events:
                if more_button.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        page += 1
                        switch = 0 # have to load the images of the new page
            if more_button.collidepoint((mx, my)):
                screen.blit(grey_right_arrow,(0.92*w,0.7475*h))
            else :
                screen.blit(black_right_arrow,(0.92*w,0.7475*h))

        ############### End of SPECIES' NAMES AND PHOTOS IN A GROUP ###############

        running = possibility_to_return_to_menu(list_of_events, running,screen, w, mx, my,
        arrow_button,arrow_back,arrow_back_grey)

        pygame.display.update()
        mainClock.tick(60)

#### End of GROUPS ###

menu()