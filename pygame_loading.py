# Loading of the images in the folder Pygames_elements and of some other values

def pygame_loading(
    pygame,
    os,
    mainClock,
    path_to_folder,
    w,
    h
    ):

    logo = pygame.image.load(
        os.path.join(path_to_folder, "Pygames_elements", "Pl@ntNet_logo.png")
    )
    logo = pygame.transform.scale(logo, (32, 32))

    pygame.display.set_icon(logo)
    window_name = "Pl@ntNet"
    pygame.display.set_caption(window_name)

    screen = pygame.display.set_mode((w, h))

    # Fonts and Colors

    mini_font = pygame.font.SysFont("timesnewroman", 20)
    medium_font = pygame.font.SysFont("timesnewroman", 27)
    big_font = pygame.font.SysFont("timesnewroman", 32)

    font = medium_font

    # Pygales Elements

    path_to_Pygame_elements = os.path.join(path_to_folder, "Pygames_elements")

    # Backgrounds

    list_of_backgrounds = []

    for i in range(1, 7):
        background = pygame.image.load(
            os.path.join(path_to_Pygame_elements, "plantnet_background_" + str(i) + ".jpg")
        )
        background_width, background_height = background.get_rect().size
        background = pygame.transform.scale(
            background, (int((background_width * h) / background_height), h)
        )
        background_width, background_height = background.get_rect().size
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

    return logo, window_name, screen, mini_font, medium_font, big_font, font, list_of_backgrounds, background_width, background_height, margin, arrow_w, arrow_h, arrow_back, arrow_back_grey, small_arrow_size, grey_right_arrow, black_right_arrow, grey_left_arrow, black_left_arrow, images_repartition, wide_logo_1, wide_logo_2, no_images