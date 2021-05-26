import pygame, sys
import os
import pandas as pd

from pygame.locals import *

###### List of functions #####

# user_paths
# draw_text

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