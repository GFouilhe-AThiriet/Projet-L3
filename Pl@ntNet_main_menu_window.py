# https://www.youtube.com/watch?v=0RryiSjpJn0
# https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame
# https://stackoverflow.com/questions/33296740/unboundlocalerror-local-variable-event-referenced-before-assignment-pygame
# https://stackoverflow.com/questions/34287938/how-to-distinguish-left-click-right-click-mouse-clicks-in-pygame
# Very interesting : https://www.reddit.com/r/pygame/comments/40873s/could_you_explain_for_event_in_pygameeventget/
# https://stackoverflow.com/questions/42215932/two-for-event-in-pygame-event-get

import pygame, sys
import os
import pandas as pd
import numpy as np

from functions import *
from pygame.locals import *

############ Users' Parameters ############

# Complete the required paths in functions.py and then enter your name :

User = "Aurélien"

############ End of Users' Parameters ############

path_to_train, path_to_classnames, path_to_folder = user_paths(User)

# Dataframe with index, id_species, species_name, Images (number of images)
# sorted by decreasing number of images 

url = 'https://raw.githubusercontent.com/GFouilhe-AThiriet/Projet-L3/main/Miscellaneous/groups.csv'
data = pd.read_csv(url)

list_of_groups = list_of_groups(data.species_group)
print(list_of_groups)

############ Global Setup ############

screen_width = 1400 # 1400 with 0.57 ratio might be a good size
ratio = 0.57

# NB : text font won't be affected by the size of the Window.
# Thus, you might have to change the global font manually below

mainClock = pygame.time.Clock()
pygame.init()

logo = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","Pl@ntNet_logo.png"))
logo = pygame.transform.scale(logo, (100,100))

pygame.display.set_icon(logo)
window_name = "Pl@ntNet"
pygame.display.set_caption(window_name)

r = ratio
screen_height = int(screen_width*r)

w , h = screen_width , screen_height

screen = pygame.display.set_mode((screen_width,screen_height))

############ End of Global Setup ############

############ Fonts and Colors ############

medium_font = pygame.font.SysFont(None, 27)
big_font = pygame.font.SysFont(None, 50)

font = medium_font

white = (255,255,255)
black = (0,0,0)
grey = (96,119,117)
dark_grey = (64,64,64)
green = (0,200,0)
blue = (51,153,255)

############ Pygales Elements ############

list_of_backgrounds = []
for i in range(1,7):
    background = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","plantnet_background_"+str(i)+".jpg"))
    background_width , backgroundheight = background.get_rect().size
    background = pygame.transform.scale(background, (int((background_width*h)/backgroundheight),h))
    background_width , backgroundheight = background.get_rect().size
    list_of_backgrounds+=[background]

margin = w-background_width

arrow_w = int(w*0.1)
arrow_h =  int(w*0.08)
arrow_back = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","arrow_back.png"))
arrow_back = pygame.transform.scale(arrow_back, (arrow_w, arrow_h))
arrow_back_grey = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","arrow_back_grey.png"))
arrow_back_grey = pygame.transform.scale(arrow_back_grey, (arrow_w,arrow_h))

images_repartition = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","images_for_each_species.png"))
images_repartition_width = int(w*r)
images_repartition_height = int(h*r)
images_repartition = pygame.transform.scale(images_repartition,(images_repartition_width,images_repartition_height))

button_color = white # Change it from white to blue to see margin's buttons

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

#### Number of images for each species ###

def Images():
    running = True

    while running:
        screen.fill(white)
        arrow_button = pygame.Rect(0.9*w,0, arrow_w, arrow_h)

        screen.blit(images_repartition,(0.06*w,0.1*h))

        mx, my = pygame.mouse.get_pos()
        
        draw_text("(x="+str(mx)+", y="+str(my)+")", font, black, screen, 0,0.6*h)
        draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")",
        medium_font, black, screen, 0,0.7*h)
        # Useful to see positions when placing things

        if 130<=mx<=660:
            abscisses=int(((mx-130)/(660-130))*1080)
            draw_text("abscisses="+str(abscisses), medium_font, black, screen, 0.5*w,0.5*h)
            if 0<=abscisses<=1080:
                species_name = data.species_name[abscisses]
                draw_text(species_name, font, black, screen, 0.5*w,0.65*h)

                images = data.Images[abscisses]
                draw_text("Number of Images : "+str(images), font, black, screen, 0.5*w,0.55*h)

                id_species = data.id_species[abscisses]
                path_to_DIR = os.path.join(path_to_train,str(id_species))
                os.chdir(path_to_DIR)
                number_images=len(os.listdir())
                if number_images>0:
                    plant_image_jpg_name = os.listdir()[0]
                    plant_image = pygame.image.load(os.path.join(path_to_DIR,plant_image_jpg_name))
                    plant_image = pygame.transform.scale(plant_image, (int(w*0.3),int(w*0.3)))
                    screen.blit(plant_image,(0.65*w,0.2*h))
                    
        # draw_text('Number of images for each species', medium_font, black, screen, 20, 20)

        running = possibility_to_return_to_menu(running,screen,w,mx, my,
        arrow_button,arrow_back,arrow_back_grey)

        pygame.display.update()
        mainClock.tick(60)

#### End of Number of images for each species ###

#### GROUPS ###

def groups():

    j = 0

    running = True

    while running :

        screen.fill(white)
        arrow_button = pygame.Rect(0.9*w,0, arrow_w, arrow_h)

        mx, my = pygame.mouse.get_pos()

        draw_text("(x="+str(mx)+", y="+str(my)+")", font, black, screen, 0.8*w,0.6*h)
        draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")",
        medium_font, black, screen, 0.8*w,0.7*h)
        # Useful to see positions when placing things

        draw_text('Groups', font, black, screen, w*0.5, 0)

        rect = pygame.Rect(0, h*0.06,margin, h*0.1)
        pygame.draw.rect(screen, dark_grey, rect)

        list_of_events = pygame.event.get()

        for event in list_of_events:
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    print("up")
                if event.key == K_DOWN:
                    print("down")
            if mx<margin*0.6:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4 and j>0:
                        print("wheel up")
                        j+=-1
                    if event.button == 5 and j<1080:
                        print("wheel down")
                        j+=1
        
        for i in range(1,40):
            draw_text(data.species_group[i], font, black, screen, 0, h*(i+10)*0.02)

        running = possibility_to_return_to_menu(list_of_events, running,screen,w,mx, my,
        arrow_button,arrow_back,arrow_back_grey)

        pygame.display.update()
        mainClock.tick(60)

#### End of GROUPS ###

groups()