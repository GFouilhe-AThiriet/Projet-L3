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

path_to_train , path_to_folder = user_paths(User)

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

# Be careful !
# If you change these parameters, you'll have to adapt manually the position
# and size of most of the displayed elements

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

mini_font = pygame.font.SysFont("timesnewroman", 20)
medium_font = pygame.font.SysFont("timesnewroman", 27)
big_font = pygame.font.SysFont("timesnewroman", 32)

font = medium_font

# List of fonts :
# print(pygame.font.get_fonts())

white = (255,255,255)
black = (0,0,0)
light_grey = (96,119,117)
light_blue = (106,154,154)
grey = (60,60,60)
green = (0,200,0)
forest_green = (19,94,19)
light_green = (53,139,53)
blue = (51,153,255)

############# End of Fonts and Colors ##############

############ Pygales Elements ############

path_to_Pygame_elements = os.path.join(path_to_folder,"Pygames_elements")

# Backgrounds :

list_of_backgrounds = []

for i in range(1,7):
    background = pygame.image.load(os.path.join(path_to_Pygame_elements,"plantnet_background_"+str(i)+".jpg"))
    background_width , backgroundheight = background.get_rect().size
    background = pygame.transform.scale(background, (int((background_width*h)/backgroundheight),h))
    background_width , backgroundheight = background.get_rect().size
    list_of_backgrounds+=[background]

margin = w-background_width

# Arrows :

arrow_w = int(w*0.1)
arrow_h =  int(w*0.08)

arrow_back = pygame.image.load(os.path.join(path_to_Pygame_elements,"arrow_back.png"))
arrow_back = pygame.transform.scale(arrow_back, (arrow_w, arrow_h))

arrow_back_grey = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","arrow_back_grey.png"))
arrow_back_grey = pygame.transform.scale(arrow_back_grey, (arrow_w,arrow_h))

small_arrow_size = int(arrow_w*0.6)

grey_right_arrow = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","grey_right_arrow.png"))
grey_right_arrow = pygame.transform.scale(grey_right_arrow, (small_arrow_size,small_arrow_size))

black_right_arrow = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","black_right_arrow.png"))
black_right_arrow = pygame.transform.scale(black_right_arrow, (small_arrow_size,small_arrow_size))

grey_left_arrow = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","grey_left_arrow.png"))
grey_left_arrow = pygame.transform.scale(grey_left_arrow, (small_arrow_size,small_arrow_size))

black_left_arrow = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","black_left_arrow.png"))
black_left_arrow = pygame.transform.scale(black_left_arrow, (small_arrow_size,small_arrow_size))

# Number of images for each species :

images_repartition = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","images_for_each_species.png"))
images_repartition_width , images_repartition_height = images_repartition.get_size()
coeff = images_repartition_height/images_repartition_width
images_repartition = pygame.transform.scale(images_repartition,(int(0.6*w),int(0.6*w*coeff)))

# Other :

wide_logo = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","Pl@ntNet_wide_logo.png"))
logo_width , logo_height = wide_logo.get_size()
coeff = logo_height/logo_width
wide_logo_1 = pygame.transform.scale(wide_logo, (int(0.4*w),int(w*0.4*coeff)))
wide_logo_2 = pygame.transform.scale(wide_logo, (int(0.5*w),int(w*0.5*coeff)))

no_images = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","Pl@ntNet_logo.png"))
no_images = pygame.transform.scale(no_images, (int(w*0.15),int(w*0.15)))

##############################################################################
################################################## Main part of the code below
##############################################################################

############ MENU ############

def menu():

    button_color = light_green # Change it from white to blue to see margin's buttons

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

        # draw_text("(x="+str(mx)+", y="+str(my)+")", font, black, screen, 0,0.6*h,0) 
        # draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")",
        # font, black, screen, 0,0.7*h,0)
        # Please, keep that uncomment
        # It's useful to see positions when placing things

        ####### Margin #######

        first_button = pygame.Rect(0, h*0.1, margin, h*0.1)
        first_button_x , firt_button_y = margin/2 , h*0.15
        pygame.draw.rect(screen, button_color, first_button)

        if first_button.collidepoint((mx, my)):
            draw_text('Pareto Effect', big_font , grey, screen, 
            first_button_x, firt_button_y,1)
            if event.type == MOUSEBUTTONDOWN:
                Images()
        else:
            draw_text('Pareto Effect', big_font, black, screen,
            first_button_x, firt_button_y,1)

        second_button = pygame.Rect(0, h*0.25,margin, h*0.1)
        second_button_x , second_button_y = margin/2 , h*0.3
        pygame.draw.rect(screen, button_color, second_button)

        if second_button.collidepoint((mx, my)):
            draw_text('Genus', big_font, grey, screen,
            second_button_x, second_button_y,1)
            if event.type == MOUSEBUTTONDOWN:
                groups()
        else:
            draw_text('Genus', big_font, black, screen,
            second_button_x, second_button_y,1)

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
        screen.blit(wide_logo_1,(0.3*w,h*0))

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

            if 0<=abscisses<=len(data):
                species_name = str(data.species_name[abscisses])
                draw_text("Species : "+species_name, font, black, screen, 0.65*w,0.78*h,0)

                images = int(data.Images[abscisses])
                draw_text("Number of Images : "+str(images), font, black, screen, 0.65*w,0.82*h,0)

                id_species = data.id_species[abscisses]
                path_to_DIR = os.path.join(path_to_train,str(id_species))
                os.chdir(path_to_DIR)

                number_images = len(os.listdir()) # first part of gadget to change the plant photo whith right click
                if plant_representative > number_images-1:
                    plant_representative = 0

                if number_images>0: # Display of the photo of the plant-species
                    # print(len(os.listdir()))
                    plant_image_jpg_name = os.listdir()[plant_representative]
                    plant_image = pygame.image.load(os.path.join(path_to_DIR,plant_image_jpg_name))
                    plant_image = pygame.transform.scale(plant_image, (int(w*0.3),int(w*0.3)))
                    screen.blit(plant_image,(0.65*w,0.23*h))

                for event in list_of_events: # second part of the gadget to change the plant representative with right click
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 3:
                            plant_representative += 1

        running = possibility_to_return_to_menu(list_of_events, running, screen,w,mx, my,
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
    list_of_species = []

    plant_representative = np.zeros((2,4),dtype=int)
    max_plant_representative = 5 # maximum value of plant_representative+1

    interval_w = 0.02
    interval_h = 0.05

    switch = 1 # When a new group is selected, switch takes 0 as a value and Pygame loads the images
    # of the selected group

    page = 1

    short_margin = 0.15*w

    margin_color = light_blue

    additional_color = white # Change it from white to green to see additional buttons


    running = True

    while running :

        screen.fill(white)
        arrow_button = pygame.Rect(0.9*w,0, arrow_w, arrow_h)
        screen.blit(wide_logo_2,(0.25*w,0))

        margin_button = pygame.Rect(0, 0, short_margin, h)
        pygame.draw.rect(screen, margin_color, margin_button)

        mx, my = pygame.mouse.get_pos()
        
        # rect = pygame.Rect(0, h*0.06,margin, h*0.1)
        # pygame.draw.rect(screen, button_color, rect)
        # Keep that uncomment please

        # draw_text("(x="+str(mx)+", y="+str(my)+")", font, black, screen, 0.8*w,0.05*h,0)
        # draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")",
        # medium_font, black, screen, 0.8*w,0,0)
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

                        for i in range(0,45):
                            if my>h*(i+5)*0.02-0.01*h and my<h*(i+6)*0.02-0.01*h:
                                actual_group = list_of_groups[i+j]
                                index_actual_group = i+j
                                list_of_species = []
                                for k in range(len(data)):
                                    if data.species_group[k] == actual_group :
                                        list_of_species += [data.species_name[k]]

        for i in range(0,45): # Display groups' names in the margin
            draw_text(list_of_groups[i+j], mini_font, black, screen, margin/3, h*(i+5)*0.02,1)

        ### End of the Scrolling list ###

        ### Global Displayed Text ###
        
        # Title and Interactive research text (not active yet)

        draw_text("Genus",  pygame.font.SysFont("timesnewroman", 27, italic=True), black,
        screen, short_margin/2, 0.05*h, 1)

        space = interval_w + 0.15

        # Very minor visual adaptation
        # if the name of the species is very long
        textobj = font.render("Genus : "+actual_group+".", 1, black)
        textrect = textobj.get_rect()
        if textrect[2]/w > 0.17:
            space = textrect[2]/w+0.005
        # End of the Very minor visual adaptation

        draw_text("Genus : "+actual_group+".", font, black, screen, margin, h*11*0.02,0)
        draw_text("Number of species : "+str(len(list_of_species))+".", font, black, screen,
        margin+space*w, h*11*0.02,0)

        # for i in range(0,len(list_of_species)):
        #         draw_text(list_of_species[i], font, black, screen, w*0.5, h*i*0.02,0)
        # Let's keep that to control genus if necessary

        ### End of Displayed Global Text ###

        ############### SPECIES' NAMES AND PHOTOS IN A GROUP ###############
        
        more_button = pygame.Rect(0.92*w,0.7475*h, small_arrow_size, small_arrow_size)
        pygame.draw.rect(screen, additional_color, more_button)

        previous_button = pygame.Rect(0.165*w,0.7475*h, small_arrow_size, small_arrow_size)
        pygame.draw.rect(screen, additional_color, previous_button)

        ######################### Display species' photos and names #########################

        ### LOADING OF THE IMAGES FOR THE ACTUAL GROUP ###

        if switch == 0: # New group selected; Pygame has to load the images

            list_of_species_for_the_actual_group = id_species_per_group[index_actual_group]
            list_of_images_for_the_actual_group = []

            counter = 0

            list_of_rectangles = []

            small_font = pygame.font.SysFont("timesnewroman", 22)
            index_font = 22

            for p in range(2):
                sub_list_of_rectangles = []
                for i in range(4):

                    if (counter+(page-1)*8)<len(list_of_species):
                        
                        species_name = list_of_species[(counter+(page-1)*8)]

                        # Small adjustment if the name of the species is long
                        textobj = small_font.render(species_name, 1, black)
                        textrect = textobj.get_rect()
                        while textrect[2]/w > 0.17:
                            index_font-=1
                            small_font = pygame.font.SysFont("timesnewroman", index_font)
                            textobj = small_font.render(species_name, 1, black)
                            textrect = textobj.get_rect()
                        #End of the small adjust

                        rect = pygame.Rect(margin+i*(0.15+interval_w)*w, 0.27*h+p*(0.27+interval_h)*h, w*0.15, w*0.15 )
                        # pygame.draw.rect(screen, green, rect)
                        # Keep that comment please
                        sub_list_of_rectangles +=[rect]

                        path_to_DIR = os.path.join(path_to_train,str(list_of_species_for_the_actual_group[counter+(page-1)*8]))

                        os.chdir(path_to_DIR)

                        number_images = len(os.listdir()) # number of images for ONE species

                        if plant_representative[p][i] > min(number_images-1,max_plant_representative-1):
                            plant_representative[p][i] = 0

                        if number_images > 0 :
                            list_of_images_of_the_same_species = []
                            for m in range(min(number_images,max_plant_representative)):
                                plant_image_jpg_name = os.listdir()[m]
                                plant_image = pygame.image.load(os.path.join(path_to_DIR,plant_image_jpg_name))
                                plant_image = pygame.transform.scale(plant_image, (int(w*0.15),int(w*0.15)))
                                list_of_images_of_the_same_species += [plant_image]
                            list_of_images_for_the_actual_group += [list_of_images_of_the_same_species]
                        else :
                            list_of_images_for_the_actual_group += [False] # No images for this species
                            
                        counter+=1

                list_of_rectangles += [sub_list_of_rectangles]

            # print(plant_representative)

            switch = 1 # no need to load again the images for Pygame until another group is selected

        ### End of LOADING OF THE IMAGES FOR THE ACTUAL GROUP ###

        ####### Display of the images of this group #######

        counter = 0

        for p in range(2):
            for i in range(4):
                if (counter+(page-1)*8)<len(list_of_species):
                    # Display one image and the species' name
                    if list_of_images_for_the_actual_group[counter] != False:
                        # print(list_of_images_for_the_actual_group[counter])
                        # print(plant_representative[p][i])
                        screen.blit(list_of_images_for_the_actual_group[counter][plant_representative[p][i]],
                        (margin+i*(0.15+interval_w)*w, 0.27*h+p*(0.27+interval_h)*h))
                    else:
                        screen.blit(no_images,
                        (margin+i*(0.15+interval_w)*w, 0.27*h+p*(0.27+interval_h)*h))
                    
                    species_name = list_of_species[counter+(page-1)*8]

                    draw_text(species_name,
                    small_font, black, screen,
                    margin+i*(0.15+interval_w)*w+0.075*w, 2*0.27*h+p*(0.27+interval_h)*h+0.02*h, 1)
                    # End of Display one image and the species' name

                    rect = list_of_rectangles[p][i]

                    for event in list_of_events:
                        if rect.collidepoint((mx, my)):
                            if event.type == MOUSEBUTTONDOWN:
                                if event.button == 3:
                                    plant_representative[p][i] += 1
                                    switch = 0

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