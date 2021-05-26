import pygame, sys
import os
import pandas as pd

###### List of functions #####

# user_paths
# draw_text
# return_main_menu_possibility()

############# END #############

###################################################################################

def user_paths(User):
        
    if User=="Aurélien":
        path_to_train = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset','python','train')
        path_to_classnames = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset')
        path_to_folder=os.path.join('C:','\\Users','lyz50',"documents","Github","Projet-L3")
    elif User=="Guilhem":
        path_to_train = os.path.join('C:/','Plantnet_project','plantnet_subset')
        path_to_classnames = os.path.join('C:/','Plantnet_project')
        path_to_folder= os.path.join('C:','\\Users\guilh\OneDrive\Documents\GitHub\Projet-L3')
    elif User=="Joseph":
        path_to_train = os.path.join("/home","jsalmon","Documents","Datasets","train")
        path_to_classnames = os.path.join("/home","jsalmon","Documents","...")
        path_to_folder=os.path.join("...")
    elif User=="Camille":
        path_to_train = os.path.join("...")
        path_to_classnames = os.path.join("...")
        path_to_folder=os.path.join("...")
    return ((path_to_train,path_to_classnames,path_to_folder))

###################################################################################

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

###################################################################################

def return_main_menu_possibility(arrow_back,arrow_back_grey,w,r):
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