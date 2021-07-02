import pygame, sys
import os
import pandas as pd
import numpy as np

from functions import *
from pygame.locals import *

from Images import *
from groups import *

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


# Global Setup

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


screen_width = 1400  # 1400 with 0.57 ratio might be a good size
ratio = 0.57

# Be careful !
# If you change these parameters, you'll have to adapt manually the position
# and size of most of the displayed elements

mainClock = pygame.time.Clock()
pygame.init()

logo = pygame.image.load(
    os.path.join(path_to_folder, "Pygames_elements", "Pl@ntNet_logo.png")
)
logo = pygame.transform.scale(logo, (32, 32))

pygame.display.set_icon(logo)
window_name = "Pl@ntNet"
pygame.display.set_caption(window_name)

r = ratio
screen_height = int(screen_width * r)

w, h = screen_width, screen_height

screen = pygame.display.set_mode((screen_width, screen_height))

# Fonts and Colors

mini_font = pygame.font.SysFont("timesnewroman", 20)
medium_font = pygame.font.SysFont("timesnewroman", 27)
big_font = pygame.font.SysFont("timesnewroman", 32)

font = medium_font

# List of fonts
# print(pygame.font.get_fonts())

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


# Pygales Elements

path_to_Pygame_elements = os.path.join(path_to_folder, "Pygames_elements")

# Backgrounds

list_of_backgrounds = []

for i in range(1, 7):
    background = pygame.image.load(
        os.path.join(path_to_Pygame_elements, "plantnet_background_" + str(i) + ".jpg")
    )
    background_width, backgroundheight = background.get_rect().size
    background = pygame.transform.scale(
        background, (int((background_width * h) / backgroundheight), h)
    )
    background_width, backgroundheight = background.get_rect().size
    list_of_backgrounds += [background]

margin = w - background_width

# Arrows :

arrow_w = int(w * 0.1)
arrow_h = int(w * 0.08)

arrow_back = pygame.image.load(os.path.join(path_to_Pygame_elements, "arrow_back.png"))
arrow_back = pygame.transform.scale(arrow_back, (arrow_w, arrow_h))

arrow_back_grey = pygame.image.load(
    os.path.join(path_to_folder, "Pygames_elements", "arrow_back_grey.png")
)
arrow_back_grey = pygame.transform.scale(arrow_back_grey, (arrow_w, arrow_h))

small_arrow_size = int(arrow_w * 0.6)

grey_right_arrow = pygame.image.load(
    os.path.join(path_to_folder, "Pygames_elements", "grey_right_arrow.png")
)
grey_right_arrow = pygame.transform.scale(
    grey_right_arrow, (small_arrow_size, small_arrow_size)
)

black_right_arrow = pygame.image.load(
    os.path.join(path_to_folder, "Pygames_elements", "black_right_arrow.png")
)
black_right_arrow = pygame.transform.scale(
    black_right_arrow, (small_arrow_size, small_arrow_size)
)

grey_left_arrow = pygame.image.load(
    os.path.join(path_to_folder, "Pygames_elements", "grey_left_arrow.png")
)
grey_left_arrow = pygame.transform.scale(
    grey_left_arrow, (small_arrow_size, small_arrow_size)
)

black_left_arrow = pygame.image.load(
    os.path.join(path_to_folder, "Pygames_elements", "black_left_arrow.png")
)
black_left_arrow = pygame.transform.scale(
    black_left_arrow, (small_arrow_size, small_arrow_size)
)

# Number of images for each species

images_repartition = pygame.image.load(
    os.path.join(path_to_folder, "Pygames_elements", "images_for_each_species.png")
)
images_repartition_width, images_repartition_height = images_repartition.get_size()
coef = images_repartition_height / images_repartition_width
images_repartition = pygame.transform.scale(
    images_repartition, (int(0.6 * w), int(0.6 * w * coef))
)

# Other

wide_logo = pygame.image.load(
    os.path.join(path_to_folder, "Pygames_elements", "Pl@ntNet_wide_logo.png")
)
logo_width, logo_height = wide_logo.get_size()
coef = logo_height / logo_width
wide_logo_1 = pygame.transform.scale(wide_logo, (int(0.4 * w), int(w * 0.4 * coef)))
wide_logo_2 = pygame.transform.scale(wide_logo, (int(0.5 * w), int(w * 0.5 * coef)))

no_images = pygame.image.load(
    os.path.join(path_to_folder, "Pygames_elements", "Pl@ntNet_logo.png")
)
no_images = pygame.transform.scale(no_images, (int(w * 0.15), int(w * 0.15)))

##############################################################################
################################################## Main part of the code below
##############################################################################

############ MENU ############


def menu():

    sub_choice = False

    button_color = (
        light_green  # Change it from white to light_green to see margin's buttons
    )

    background_index = np.random.randint(0, 6)  # Initialisation

    while True:
        screen = pygame.display.set_mode((screen_width, screen_height))
        screen.fill(white)

        mx, my = pygame.mouse.get_pos()

        background_button = pygame.Rect(margin, 0, background_width, backgroundheight)
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
                    print("gauuche")
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
                    print("droooite")
            else:
                draw_text("3D",big_font, black, screen, right_text_x, right_text_y, 1)
                

        # End of Interactions ###

        pygame.display.update()
        mainClock.tick(60)

menu()
