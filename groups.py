# Visualisation of the dataset ###

def groups(   
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
    possibility_to_return_to_menu
    ):

    order = 2
    order_text = "ABC"
    id_species_per_group = id_species_per_group_order_2
    list_of_groups = list_of_groups_order_2

    j = 0
    actual_group = "not initialised"
    index_actual_group = 0
    list_of_species = []

    plant_representative = np.zeros((2, 4), dtype=int)
    max_plant_representative = 5  # maximum value of plant_representative+1

    interval_w = 0.02
    interval_h = 0.05

    switch = 1  # When selecting new group, switch to 0 and Pygame loads images
    # of the selected group

    page = 1

    short_margin = 0.15 * w

    margin_color = light_blue

    additional_color = white  # Change from white to green to see more_button

    running = True

    while running:

        screen.fill(white)
        arrow_button = pygame.Rect(0.9 * w, 0, arrow_w, arrow_h)
        screen.blit(wide_logo_2, (0.25 * w, 0))

        margin_button = pygame.Rect(0, 0, short_margin, h)
        pygame.draw.rect(screen, margin_color, margin_button)

        mx, my = pygame.mouse.get_pos()

        # rect = pygame.Rect(0, h*0.06,margin, h*0.1)
        # pygame.draw.rect(screen, button_color, rect)
        # Keep that uncomment please

        order_button = pygame.Rect(w * 0.165, h * 0.025, w * 0.033, w * 0.033)
        pygame.draw.rect(screen, light_green, order_button)
        draw_text(order_text, mini_font, black, screen, w * 0.182, h * 0.053, 1)
        # To change the order of the scrolling list

        # draw_text("(x="+str(mx)+", y="+str(my)+")", font, black, screen, 0.8*w,0.05*h,0)
        # draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")",
        # medium_font, black, screen, 0.8*w,0,0)
        # Useful to see positions when placing things

        list_of_events = pygame.event.get()

        ### Scrolling list ###

        for event in list_of_events:
            if event.type == KEYDOWN:
                if event.key == K_UP and j > 0:
                    j += -1
                if event.key == K_DOWN and j < len(list_of_groups) - 40:
                    j += 1

            # Possibility to change the order of the scrolling list
            if order_button.collidepoint((mx, my)):
                if event.type == MOUSEBUTTONDOWN:
                    if order == 1:
                        order = 2
                        list_of_groups = list_of_groups_order_2
                        id_species_per_group = id_species_per_group_order_2
                        order_text = "ABC"
                    else:  # order = 2
                        order = 1
                        list_of_groups = list_of_groups_order_1
                        id_species_per_group = id_species_per_group_order_1
                        order_text = "123"
            # End of Possibility to change the order of the scrolling list

            if mx < margin * 0.6:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4 and j > 0:
                        j += -1
                    if event.button == 5 and j < len(list_of_groups) - 45:
                        j += 1
                    if event.button == 1:

                        switch = 0  # in order that the loading of the images is only done once

                        page = 1

                        for i in range(0, 45):
                            if (
                                my > h * (i + 5) * 0.02 - 0.01 * h
                                and my < h * (i + 6) * 0.02 - 0.01 * h
                            ):
                                actual_group = list_of_groups[i + j]
                                index_actual_group = i + j
                                list_of_species = []
                                for k in range(len(data)):
                                    if data.genus[k] == actual_group:
                                        list_of_species += [data.species_name[k]]

        for i in range(0, 45):  # Display groups' names in the margin
            draw_text(
                list_of_groups[i + j],
                mini_font,
                black,
                screen,
                margin / 3,
                h * (i + 5) * 0.02,
                1,
            )

        # Global Displayed Text

        # Title

        draw_text(
            "Genus",
            pygame.font.SysFont("timesnewroman", 27, italic=True),
            black,
            screen,
            short_margin / 2,
            0.05 * h,
            1,
        )

        space = interval_w + 0.15

        # Very minor visual adaptation
        # if the name of the species is very long
        textobj = font.render("Genus : " + actual_group + ".", 1, black)
        textrect = textobj.get_rect()
        if textrect[2] / w > 0.17:
            space = textrect[2] / w + 0.005
        # End of the Very minor visual adaptation

        draw_text(
            "Genus : " + actual_group + ".",
            font,
            black,
            screen,
            margin,
            h * 11 * 0.02,
            0,
        )
        draw_text(
            "Number of species : " + str(len(list_of_species)) + ".",
            font,
            black,
            screen,
            margin + space * w,
            h * 11 * 0.02,
            0,
        )

        # for i in range(0,len(list_of_species)):
        #         draw_text(list_of_species[i], font, black, screen, w*0.5, h*i*0.02,0)
        # Let's keep that to control genus if necessary

        # SPECIES' NAMES AND PHOTOS IN A GROUP

        more_button = pygame.Rect(
            0.92 * w, 0.7475 * h, small_arrow_size, small_arrow_size
        )
        pygame.draw.rect(screen, additional_color, more_button)

        previous_button = pygame.Rect(
            0.165 * w, 0.7475 * h, small_arrow_size, small_arrow_size
        )
        pygame.draw.rect(screen, additional_color, previous_button)

        # Display species' photos and names

        # LOADING OF THE IMAGES FOR THE ACTUAL GROUP

        if switch == 0:  # New group selected; Pygame has to load the images

            list_of_species_for_the_actual_group = id_species_per_group[
                index_actual_group
            ]
            list_of_images_for_the_actual_group = []

            counter = 0

            list_of_rectangles = []

            small_font = pygame.font.SysFont("timesnewroman", 22)
            index_font = 22

            for p in range(2):
                sub_list_of_rectangles = []
                for i in range(4):

                    if (counter + (page - 1) * 8) < len(list_of_species):

                        species_name = list_of_species[(counter + (page - 1) * 8)]

                        # Small adjustment if the name of the species is long
                        textobj = small_font.render(species_name, 1, black)
                        textrect = textobj.get_rect()
                        while textrect[2] / w > 0.17:
                            index_font -= 1
                            small_font = pygame.font.SysFont(
                                "timesnewroman", index_font
                            )
                            textobj = small_font.render(species_name, 1, black)
                            textrect = textobj.get_rect()
                        # End of the small adjustment

                        rect = pygame.Rect(
                            margin + i * (0.15 + interval_w) * w,
                            0.27 * h + p * (0.27 + interval_h) * h,
                            w * 0.15,
                            w * 0.15,
                        )
                        # pygame.draw.rect(screen, green, rect)
                        # Keep that comment please
                        sub_list_of_rectangles += [rect]

                        path_to_DIR = os.path.join(
                            path_to_train,
                            str(
                                list_of_species_for_the_actual_group[
                                    counter + (page - 1) * 8
                                ]
                            ),
                        )

                        os.chdir(path_to_DIR)

                        number_images = len(
                            os.listdir()
                        )  # number of images for ONE species

                        if plant_representative[p][i] > min(
                            number_images - 1, max_plant_representative - 1
                        ):
                            plant_representative[p][i] = 0

                        if number_images > 0:
                            list_of_images_of_the_same_species = []
                            for m in range(
                                min(number_images, max_plant_representative)
                            ):
                                plant_image_jpg_name = os.listdir()[m]
                                plant_image = pygame.image.load(
                                    os.path.join(path_to_DIR, plant_image_jpg_name)
                                )
                                plant_image = pygame.transform.scale(
                                    plant_image, (int(w * 0.15), int(w * 0.15))
                                )
                                list_of_images_of_the_same_species += [plant_image]
                            list_of_images_for_the_actual_group += [
                                list_of_images_of_the_same_species
                            ]
                        else:
                            list_of_images_for_the_actual_group += [
                                False
                            ]  # No images for this species

                        counter += 1

                list_of_rectangles += [sub_list_of_rectangles]

            # print(plant_representative)

            switch = 1  # no need to load images again until another group is selected

        # Display of the images of this group #######

        counter = 0

        for p in range(2):
            for i in range(4):
                if (counter + (page - 1) * 8) < len(list_of_species):
                    # Display one image and the species' name
                    if list_of_images_for_the_actual_group[counter] != False:
                        # print(list_of_images_for_the_actual_group[counter])
                        # print(plant_representative[p][i])
                        screen.blit(
                            list_of_images_for_the_actual_group[counter][
                                plant_representative[p][i]
                            ],
                            (
                                margin + i * (0.15 + interval_w) * w,
                                0.27 * h + p * (0.27 + interval_h) * h,
                            ),
                        )
                    else:
                        screen.blit(
                            no_images,
                            (
                                margin + i * (0.15 + interval_w) * w,
                                0.27 * h + p * (0.27 + interval_h) * h,
                            ),
                        )

                    species_name = list_of_species[counter + (page - 1) * 8]

                    draw_text(
                        species_name,
                        small_font,
                        black,
                        screen,
                        margin + i * (0.15 + interval_w) * w + 0.075 * w,
                        2 * 0.27 * h + p * (0.27 + interval_h) * h + 0.02 * h,
                        1,
                    )
                    # End of Display one image and the species' name

                    rect = list_of_rectangles[p][i]

                    for event in list_of_events:
                        if rect.collidepoint((mx, my)):
                            if event.type == MOUSEBUTTONDOWN:
                                if event.button == 3:
                                    plant_representative[p][i] += 1
                                    switch = 0

                    counter += 1

        # If there are more than 8 images to display ###

        if page > 1:  # need to have the possibility to come back to the previous window
            for event in list_of_events:
                if previous_button.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        page += -1
                        switch = 0  # have to load the images of the new page
            if previous_button.collidepoint((mx, my)):
                screen.blit(grey_left_arrow, (0.165 * w, 0.7475 * h))
            else:
                screen.blit(black_left_arrow, (0.165 * w, 0.7475 * h))

        if (
            len(list_of_species) - 8 * page
        ) >= 1:  # then, need to have an additional window
            for event in list_of_events:
                if more_button.collidepoint((mx, my)):
                    if event.type == MOUSEBUTTONDOWN:
                        page += 1
                        switch = 0  # have to load the images of the new page
            if more_button.collidepoint((mx, my)):
                screen.blit(grey_right_arrow, (0.92 * w, 0.7475 * h))
            else:
                screen.blit(black_right_arrow, (0.92 * w, 0.7475 * h))

        ############### End of SPECIES' NAMES AND PHOTOS IN A GROUP ###############

        running = possibility_to_return_to_menu(
            list_of_events,
            running,
            screen,
            w,
            mx,
            my,
            arrow_button,
            arrow_back,
            arrow_back_grey,
        )

        pygame.display.update()
        mainClock.tick(60)