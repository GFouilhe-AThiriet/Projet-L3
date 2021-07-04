import pygame, sys
import os
import pandas as pd
import numpy as np

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
        path_to_train = os.path.join('C:','\\Users','lyz50','Documents',"train")

        path_to_folder=os.path.join('C:','\\Users','lyz50',"documents","Github","Projet-L3")
    elif User == "Guilhem":
        path_to_train = os.path.join('C:/','Plantnet_project','plantnet_subset')
        path_to_folder= os.path.join('C:','\\Users\guilh\OneDrive\Documents\GitHub\Projet-L3')
    elif User == "Joseph":
        path_to_train = os.path.join("/home","jsalmon","Documents","Datasets","train")
        path_to_folder=os.path.join("/home/jsalmon/Documents/Mes_cours/Montpellier/Stages/L3/Projet-L3")
    elif User == "Camille":
        path_to_train = os.path.join(r"C:\Users\cgarc\top-k-classification\Python\data\big_plantnet\train")
        path_to_folder=os.path.join(r"C:\Users\cgarc\Projet-L3")
    return ((path_to_train,path_to_folder))

###################################################################################

def draw_text(text, font, color, surface, x, y, center):

    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()

    if center == True : # (x,y) will be the center of the rectangle
        textrect.center = (x, y)
    else: # (x,y) will be the topleft corner of the rectangle
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

def make_a_list_of_groups(serie):
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

def make_id_species_per_group(list_of_id_species,sorted_list_of_species_group,list_of_groups):
    L = []
    for i in range(len(list_of_groups)):
        H = []
        for j in range(len(sorted_list_of_species_group)):
            if sorted_list_of_species_group[j] == list_of_groups[i]:
                H += [list_of_id_species[j]]
        L += [H]
    return L

###################################################################################

##### This function is not OK is the current state
# As the precision of mouse coordinates is very bad,
# I don't even know if the result would be satisfying if it was

def decipher_coord(coords,data,dim): #coords is a string

    if dim == 2:

        error_limit = 2
        
        index = "not found"

        for i in range(len(coords)):
            if coords[i] == "x":
                pos_x = i
            if coords[i] == "y":
                pos_y = i

        a,b = coords[pos_x+3:pos_y-1],coords[pos_y+3:len(coords)]
        if coords[pos_x+2] == "−" or coords[pos_x+2] == "-":
            a = "-" + a
        else:
            a = coords[pos_x+2] + a
        if coords[pos_y+2] == "−" or coords[pos_y+2] == "-":
            b = "-" + b
        else:
            b = coords[pos_y+2] + b
        c = 0

        # transform the string "x=36.0244, y=−17.0519"
        # in the 3 strings a="36.02",b="17.05"

        error = 0
        
        while index == "not found" :
            
            i = 0
            loop = True
            while i < len(data)-1 and loop == True:
                if (
                    (data._2D_tsne_1[i]-float(a))**2
                    + (data._2D_tsne_2[i]-float(b))**2
                    < error
                    ):
                    index = i
                    loop = False # to end the loop
                i += 1

            error += 0.02
            if error > error_limit:
                index = 0
                error = "too big"

    if dim == 3:

        error_limit = 30
        
        index = "not found"

        for i in range(len(coords)):
            if coords[i] == "x":
                pos_x = i
            if coords[i] == "y":
                pos_y = i
            if coords[i] == "z":
                pos_z = i
        a,b,c = coords[pos_x+3:pos_y-2],coords[pos_y+3:pos_z-2],coords[pos_z+3:len(coords)]
        if coords[pos_x+2] == "−" or coords[pos_x+2] == "-":
            a = "-" + a
        else:
            a = coords[pos_x+2] + a
        if coords[pos_y+2] == "−" or coords[pos_y+2] == "-":
            b = "-" + b
        else:
            b = coords[pos_y+2] + b
        if coords[pos_z+2] == "−" or coords[pos_z+2] == "-":
            c = "-" + c
        else:
            c = coords[pos_z+2] + c
        # transform the string "x=36.0244, y=−17.0519, z=36.9563"
        # in the 3 strings a="36.02",b="17.05", and c="36.95"

        error = 0

        while index == "not found" :
            
            i = 0
            loop = True
            while i < len(data)-1 and loop == True:
                if (
                    (data._3D_tsne_1[i]-float(a))**2
                    + (data._3D_tsne_2[i]-float(b))**2
                    + (data._3D_tsne_3[i]-float(c))**2
                    < error
                    ):
                    index = i
                    loop = False # to end the loop
                i += 1

            error += 0.5
            if error > error_limit:
                index = 0
                error = "too big"

    return a, b, c, index , error