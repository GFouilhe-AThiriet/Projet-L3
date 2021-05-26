# https://www.youtube.com/watch?v=0RryiSjpJn0
# https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame

import pygame, sys
import os
import pandas as pd
from functions import user_path

User = "Guilhem"
path_to_train,path_to_classnames, path_to_folder = user_path(User)



#Dataframe with index, id_species, species_name, Images (number of images) sorted by decreasing number of images 
url = 'https://raw.githubusercontent.com/GFouilhe-AThiriet/Projet-L3/main/data.csv'
data = pd.read_csv(url)

### Global Setup ###

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

logo = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","Pl@ntNet_logo.png"))
logo = pygame.transform.scale(logo, (100,100))

pygame.display.set_icon(logo)
window_name = "Pl@ntNet"
pygame.display.set_caption(window_name)

###ADJUST THE SIZE OF THE WINDOW BY CHANGING THE FOLLOWING VALUE :

screen_width = 800
ratio=0.8

### End of Global Setup ###

r=ratio
screen_height = int(screen_width*r)

w , h = screen_width , screen_height

screen = pygame.display.set_mode((screen_width,screen_height))
 
font = pygame.font.SysFont(None, 50)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

#### Pygales Elements ####

background = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","plantnet_background.jpg"))
background = pygame.transform.scale(background, (screen_width,screen_height))

arrow_back = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","arrow_back.png"))
arrow_back = pygame.transform.scale(arrow_back, (int(w*0.1),int(h*0.1)))
arrow_back_grey = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","arrow_back_grey.png"))
arrow_back_grey = pygame.transform.scale(arrow_back_grey, (int(w*0.1),int(h*0.1)))

images_repartition = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","images_for_each_species.png"))
images_repartition_width = int(w*r)
images_repartition_height = int(h*r)
images_repartition = pygame.transform.scale(images_repartition,(images_repartition_width,images_repartition_height))

white = (255,255,255)
black = (0,0,0)
grey = (96,119,117)

#### MENU #### 

def menu():
    
    while True:
        screen = pygame.display.set_mode((screen_width,screen_height))
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
 
        mx, my = pygame.mouse.get_pos()
        #draw_text("(x="+str(mx)+", y="+str(my)+")", font, white, screen, 0,0.6*h)
        #draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")", font, white, screen, 0,0.7*h)

        # reference_square = pygame.Rect(w*0.8, h*0.1 , w*0.1, h*0.1)# x_pos,y_pos,width,height
        # pygame.draw.rect(screen, (255, 255, 255), reference_square)

        Images_button = pygame.Rect(w*0.1, h*0.1,w*0.8, h*0.1)
        pygame.draw.rect(screen, (255, 255, 255), Images_button)

        #Number of images for each species
        if Images_button.collidepoint((mx, my)):
            draw_text('Number of images for each species', font, grey, screen, 0.13*w, 0.13*h)
            if event.type == MOUSEBUTTONDOWN:
                Images()
        else:
            draw_text('Number of images for each species', font, black, screen, 0.13*w, 0.13*h)

        #Groups
        Groups_button = pygame.Rect(w*0.1, h*0.3,w*0.2 , h*0.1)
        pygame.draw.rect(screen, (255, 255, 255), Groups_button)

        if Groups_button.collidepoint((mx, my)):
            draw_text('Groups', font, grey, screen, 0.13*w, 0.33*h)
            if event.type == MOUSEBUTTONDOWN:
                groups()
        else:
            draw_text('Groups', font, black, screen, 0.13*w, 0.33*h)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
 
        pygame.display.update()
        mainClock.tick(60)

#### Number of images for each species ###

def Images():
    running = True

    while running:
        screen.fill(white)
        arrow_button = pygame.Rect(0.9*w,0, w*0.1 , h*0.1)

        screen.blit(images_repartition,(0.06*w,0.1*h))

        mx, my = pygame.mouse.get_pos()
        #draw_text("(x="+str(mx)+", y="+str(my)+")", font, black, screen, 0,0.6*h)
        #draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")", font, black, screen, 0,0.7*h)

        if 130<=mx<=660:
            abscisses=int(((mx-130)/(660-130))*1080)
            draw_text("abscisses="+str(abscisses), font, black, screen, 0.5*w,0.5*h)
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
                    plant_image = pygame.transform.scale(plant_image, (int(w*0.3),int(h*0.3)))
                    screen.blit(plant_image,(0.65*w,0.2*h))
                    
        # draw_text('Number of images for each species', font, black, screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if arrow_button.collidepoint((mx, my)):
                if event.type == MOUSEBUTTONDOWN:
                    running = False
        if arrow_button.collidepoint((mx, my)):
            screen.blit(arrow_back_grey,(0.9*w,0))
        else :
            screen.blit(arrow_back,(0.9*w,0))

        pygame.display.update()
        mainClock.tick(60)

#### End of Number of images for each species ###

#### GROUPS ###

def groups():
    running = True
    while running:
        screen.fill(white)
        arrow_button = pygame.Rect(0.9*w,0, w*0.1 , h*0.1)

        mx, my = pygame.mouse.get_pos()

        draw_text('Groups', font, black, screen, 20, 20)

        rectangle = pygame.Rect(w*0.2, h*0.1,w*0.6, h*0.2)
        pygame.draw.rect(screen, grey, rectangle)
        draw_text("Coquelicot", pygame.font.SysFont(None, 30), black, screen, 0.3*w,0.15*h)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if arrow_button.collidepoint((mx, my)):
                if event.type == MOUSEBUTTONDOWN:
                    running = False
        if arrow_button.collidepoint((mx, my)):
            screen.blit(arrow_back_grey,(0.9*w,0))
        else :
            screen.blit(arrow_back,(0.9*w,0))

        pygame.display.update()
        mainClock.tick(60)

#### End of GROUPS ###

menu()