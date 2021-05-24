# https://www.youtube.com/watch?v=0RryiSjpJn0
# https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame

import pygame, sys
import os

User = "Aurélien"

if User=="Aurélien":
    path_to_train = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset','python','train')
    path_to_classnames = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset')
    path_to_folder=os.path.join('C:','\\Users','lyz50',"documents","Github","Projet-L3")
elif User=="Guilhem":
    path_to_train = os.path.join('C:/','Plantnet_project','plantnet_subset')
    path_to_classnames = os.path.join('C:/','Plantnet_project')
    path_to_folder=os.path.join("...")
elif User=="Joseph":
    path_to_train = os.path.join("/home","jsalmon","Documents","Datasets","train")
    path_to_classnames = os.path.join("/home","jsalmon","Documents","...")
    path_to_folder=os.path.join("...")
elif User=="Camille":
    path_to_train = os.path.join("...")
    path_to_classnames = os.path.join("...")
    path_to_folder=os.path.join("...")

path_to_folder=os.path.join('C:','\\Users','lyz50',"documents","Github","Projet-L3")

### Global Setup ###

mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()

window_name = "Pl@ntNet"

pygame.display.set_caption(window_name)

#NB; to do : change the pygame icon by the plantnet icon
#https://stackoverflow.com/questions/21271059/how-do-i-change-the-pygame-icon

###ADJUST THE SIZE OF THE WINDOW BY CHANGING THE FOLLOWING VALUE :

screen_width = 1000

### End of Global Setup ###

screen_height = int(screen_width*0.8)

w , h = screen_width , screen_height

screen = pygame.display.set_mode((screen_width,screen_height))
 
font = pygame.font.SysFont(None, 50)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False

#### Elements ####

background = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","plantnet_background.jpg"))
background = pygame.transform.scale(background, (screen_width,screen_height))

arrow_back = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","arrow_back.png"))
arrow_back = pygame.transform.scale(arrow_back, (int(w*0.1),int(h*0.1)))
arrow_back_grey = pygame.image.load(os.path.join(path_to_folder,"Pygames_elements","arrow_back_grey.png"))
arrow_back_grey = pygame.transform.scale(arrow_back_grey, (int(w*0.1),int(h*0.1)))


white = (255,255,255)
black = (0,0,0)
grey = (96,119,117)

#### MENU #### 

def menu():

    while True:
 
        screen.fill((0,0,0))
        screen.blit(background,(0,0))
 
        mx, my = pygame.mouse.get_pos()
        draw_text("(x="+str(mx)+", y="+str(my)+")", font, white, screen, 0,0.6*h)
        draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")", font, white, screen, 0,0.7*h)

        reference_square = pygame.Rect(w*0.8, h*0.1 , w*0.1, h*0.1)# x_pos,y_pos,width,height
        pygame.draw.rect(screen, (255, 255, 255), reference_square)

        Groups_button = pygame.Rect(w*0.1, h*0.1,w*0.2 , h*0.1)
        pygame.draw.rect(screen, (255, 255, 255), Groups_button)

        if Groups_button.collidepoint((mx, my)):
            draw_text('Groups', font, grey, screen, 0.13*w, 0.13*h)
            if event.type == MOUSEBUTTONDOWN:
                groups()
        else:
            draw_text('Groups', font, black, screen, 0.13*w, 0.13*h)


        click = False
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
 
def groups():
    running = True
    while running:
        screen.fill(white)
        arrow_button = pygame.Rect(0.8*w,0.1*h, w*0.1 , h*0.1)

        mx, my = pygame.mouse.get_pos()

        draw_text('Groups', font, black, screen, 20, 20)

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
            screen.blit(arrow_back_grey,(0.8*w,0.1*h))
        else :
            screen.blit(arrow_back,(0.8*w,0.1*h))

        pygame.display.update()
        mainClock.tick(60)
 
menu()