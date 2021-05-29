import pygame, sys
import os
import pandas as pd

from pygame.locals import *

###### List of functions #####

# user_paths
# draw_text
# possibility_to_return_to_menu
# list_of_groups(serie)
# id_species_per_group

############# END #############

###################################################################################

def user_paths(User):
        
    if User=="Aurélien":
        path_to_train = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset','python','train')
        path_to_folder=os.path.join('C:','\\Users','lyz50',"documents","Github","Projet-L3")
    elif User=="Guilhem":
        path_to_train = os.path.join('C:/','Plantnet_project','plantnet_subset')
        path_to_folder= os.path.join('C:','\\Users\guilh\OneDrive\Documents\GitHub\Projet-L3')
    elif User=="Joseph":
        path_to_train = os.path.join("/home","jsalmon","Documents","Datasets","train")
        path_to_folder=os.path.join("...")
    elif User=="Camille":
        path_to_train = os.path.join("...")
        path_to_folder=os.path.join("...")
    return ((path_to_train,path_to_folder))

###################################################################################

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

###################################################################################

def possibility_to_return_to_menu(list_of_events,running,screen,w,mx, my,arrow_button,arrow_back,arrow_back_grey):

    for event in list_of_events:
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

    return running

###################################################################################

def list_of_groups(serie):
    a=[]
    for i in range(len(serie)):
        switch=0
        for j in range(len(a)):
            if a[j]==serie[i]:
                    switch=1
        if switch==0:
            a+=[serie[i]]
    return a

# to do : sorting the list by decreasing number of species ?

###################################################################################

def id_species_per_group(list_of_id_species,sorted_list_of_species_group,list_of_groups):
    L = []
    for i in range(len(list_of_groups)):
        H = []
        for j in range(len(sorted_list_of_species_group)):
            if sorted_list_of_species_group[j] == list_of_groups[i]:
                H += [list_of_id_species[j]]
        L += [H]
    return L

