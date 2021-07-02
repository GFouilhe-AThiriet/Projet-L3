import pygame, sys
import os
import pandas as pd
import numpy as np

from functions import *
from pygame.locals import *

from pygame_loading import *
from Images import *
from groups import *
from display_tsne_transformation import *

# Users' Parameters

# Note : you have to download the ENTIRE subset named "TRAIN" before lauching this code
# If you have only downloaded a sample of this subset, the code should not return errors
# but a standard image will be displayed instead of a missing species' photo.

# Complete the required paths in functions.py and then enter your name :

user = "Aurélien" #input(
#     "Please type the name of the user (choose among Aurélien, Guilhem, Joseph, Camille : "
# )
# if user not in ["Aurélien", "Guilhem", "Joseph", "Camille"]:
#     raise ValueError("Incorrect username")


# Global Setup ###############################################################

path_to_train, path_to_folder = user_paths(user)

# Dataframe with index, id_species, species_name, Images (number of images)
# sorted by decreasing number of images

data = pd.read_csv(os.path.join(path_to_folder, "class_names_2.csv"))

# Load the list of genus and species for each genus

# Sorted by the decreasing order of images per genus
data.sort_values(by=["genus_images"], inplace=True, ascending=False)
data.reset_index(drop=True, inplace=True)  # Re-index
list_of_groups_order_1 = make_a_list_of_groups(data.genus)
id_species_per_group_order_1 = make_id_species_per_group(
    data.id_species, data.genus, list_of_groups_order_1
)

# Sorted by alphabetical order
data.sort_values(by=["genus"], inplace=True, ascending=True)
data.reset_index(drop=True, inplace=True)  # Re-index
list_of_groups_order_2 = make_a_list_of_groups(data.genus)
id_species_per_group_order_2 = make_id_species_per_group(
    data.id_species, data.genus, list_of_groups_order_2
)

data.sort_values(by=["Images"], inplace=True, ascending=False)
# Sorted by decreasing order of number of images
data.reset_index(drop=True, inplace=True)
# Re-index


screen_width = 1400  # 1400 with 0.57 ratio might be a good size
ratio = 0.57

# Be careful !
# If you change these parameters, you'll have to adapt manually the position
# and size of most of the displayed elements

r = ratio
screen_height = int(screen_width * r)

w, h = screen_width, screen_height

# List of colors

white = (255, 255, 255)
black = (0, 0, 0)
light_grey = (96, 119, 117)
light_blue = (106, 154, 154)
grey = (60, 60, 60)
green = (0, 200, 0)
forest_green = (19, 94, 19)
light_green = (53, 139, 53)
blue = (51, 153, 255)

# Pygame_loading ###

mainClock = pygame.time.Clock()
pygame.init()

logo, window_name, screen, mini_font, medium_font, big_font, font, list_of_backgrounds, background_width, background_height, margin, arrow_w, arrow_h, arrow_back, arrow_back_grey, small_arrow_size, grey_right_arrow, black_right_arrow, grey_left_arrow, black_left_arrow, images_repartition, wide_logo_1, wide_logo_2, no_images = pygame_loading(
    pygame,
    os,
    mainClock,
    path_to_folder,
    w,
    h
    )

# End of Global Setup ########################################################

##############################################################################
################################################## Main part of the code below
##############################################################################

############ MENU ############


def menu():

    running = True

    display_tsne_transfo = False

    sub_choice = False

    button_color = (
        light_green  # Change it from white to light_green to see margin's buttons
    )

    background_index = np.random.randint(0, 6)  # Initialisation

    while running:
        screen = pygame.display.set_mode((screen_width, screen_height))
        screen.fill(white)

        mx, my = pygame.mouse.get_pos()

        background_button = pygame.Rect(margin, 0, background_width, background_height)
        screen.blit(list_of_backgrounds[background_index], (margin, 0))
        
        for event in pygame.event.get():
            if background_button.collidepoint((mx, my)):
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    if background_index < 5:
                        background_index += 1
                    else:
                        background_index = 0
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

        # Margin

        first_button = pygame.Rect(0, h * 0.1, margin, h * 0.1)
        first_button_x, firt_button_y = margin / 2, h * 0.15
        pygame.draw.rect(screen, button_color, first_button)

        second_button = pygame.Rect(0, h * 0.25, margin, h * 0.1)
        second_button_x, second_button_y = margin / 2, h * 0.3
        pygame.draw.rect(screen, button_color, second_button)

        third_button = pygame.Rect(0, h * 0.40, margin, h * 0.1)
        third_button_x, third_button_y = margin / 2, h * 0.45
        pygame.draw.rect(screen, button_color, third_button)

        sub_square_size = w*0.05

        sub_left_button = pygame.Rect(
            margin*(1/3)-sub_square_size/2, h * 0.54,
            sub_square_size, sub_square_size)
        left_text_x, left_text_y = margin*(1/3), h * 0.54 + sub_square_size/2

        sub_right_button = pygame.Rect(
            margin*(2/3)-sub_square_size/2, h * 0.54,
            sub_square_size, sub_square_size)
        right_text_x, right_text_y = margin*(2/3), h * 0.54 + sub_square_size/2

        # Interactions ###

        # First Button

        if first_button.collidepoint((mx, my)):
            draw_text(
                "Pareto Effect",
                big_font,
                grey,
                screen,
                first_button_x,
                firt_button_y,
                1,
            )
            if event.type == MOUSEBUTTONDOWN:
                Images(
                        pygame,
                        os,
                        mainClock,
                        data,
                        path_to_train,
                        screen,
                        w,
                        h,
                        white,
                        black,
                        arrow_w,
                        arrow_h,
                        arrow_back,
                        arrow_back_grey,
                        wide_logo_1,
                        images_repartition,
                        medium_font,
                        font,
                        draw_text,
                        possibility_to_return_to_menu,
                        )
        else:
            draw_text(
                "Pareto Effect",
                big_font,
                black,
                screen,
                first_button_x,
                firt_button_y,
                1,
            )

        # Second Button

        if second_button.collidepoint((mx, my)):
            draw_text(
                "Genus", big_font, grey, screen, second_button_x, second_button_y, 1
            )
            if event.type == MOUSEBUTTONDOWN:
                groups(
                    pygame,
                    os,
                    np,
                    mainClock,
                    data,
                    path_to_train,
                    screen,
                    w,
                    h,
                    white,
                    black,
                    light_blue,
                    light_green,
                    arrow_w,
                    arrow_h,
                    arrow_back,
                    arrow_back_grey,
                    small_arrow_size,
                    grey_left_arrow,
                    black_left_arrow,
                    grey_right_arrow,
                    black_right_arrow,
                    wide_logo_2,
                    no_images,
                    list_of_groups_order_1,
                    list_of_groups_order_2,
                    id_species_per_group_order_1,
                    id_species_per_group_order_2,
                    margin,
                    mini_font,
                    font,
                    MOUSEBUTTONDOWN,
                    KEYDOWN,
                    K_UP,
                    K_DOWN,
                    draw_text,
                    possibility_to_return_to_menu,
                )
        else:
            draw_text(
                "Genus", big_font, black, screen, second_button_x, second_button_y, 1
            )

        # Third Button

        if third_button.collidepoint((mx, my)):
            draw_text(
                "TSNE transformation",
                big_font, 
                grey, 
                screen, 
                third_button_x, 
                third_button_y, 
                1
            )
            if event.type == MOUSEBUTTONDOWN:
                if sub_choice == False:
                    sub_choice = True # The choice "2D" or "3D" will be shown
                else:
                    sub_choice = False # The choice will no longer be shown
        else:
            draw_text(
                "TSNE transformation", big_font, black, screen, third_button_x, third_button_y, 1
            )

        # Sub_choice

        if sub_choice == True :
            pygame.draw.rect(screen, blue, sub_left_button)
            pygame.draw.rect(screen, blue, sub_right_button)

            if sub_left_button.collidepoint((mx, my)):
                draw_text(
                    "2D",
                    big_font, 
                    grey, 
                    screen, 
                    left_text_x, 
                    left_text_y, 
                    1
                )
                if event.type == MOUSEBUTTONDOWN:
                    display_tsne_transfo = 2
                    running = False
            else:
                draw_text("2D",big_font, black, screen, left_text_x, left_text_y, 1)
                
            
            if sub_right_button.collidepoint((mx, my)):
                draw_text(
                    "3D",
                    big_font, 
                    grey, 
                    screen, 
                    right_text_x, 
                    right_text_y, 
                    1
                )
                if event.type == MOUSEBUTTONDOWN:
                    display_tsne_transfo = 3
                    running = False
            else:
                draw_text("3D",big_font, black, screen, right_text_x, right_text_y, 1)
                
        # End of Interactions ###

        pygame.display.update()
        mainClock.tick(60)

    if display_tsne_transfo != False:
        dim = display_tsne_transfo
        tsne_transformation(data,dim)

menu()
