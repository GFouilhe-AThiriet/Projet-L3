# Pareto Effect Window ###


def Images(
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
    ):

    data.sort_values(by=["Images"], inplace=True, ascending=False)
    # Sorted by decreasing order of number of images
    data.reset_index(drop=True, inplace=True)
    # Re-index

    plant_representative = 0

    running = True

    a, b = 0.07357, 0.60285
    # y position of the y axis and of the last species' data
    # on the x axis of the displayed graph

    while running:
        screen.fill(white)
        arrow_button = pygame.Rect(0.9 * w, 0, arrow_w, arrow_h)
        screen.blit(wide_logo_1, (0.3 * w, h * 0))

        screen.blit(images_repartition, (0.03 * w, 0.19 * h))  # the graph
        draw_text(
            "Number of images for each species",
            medium_font,
            black,
            screen,
            0.35 * w,
            0.175 * h,
            1,
        )

        mx, my = pygame.mouse.get_pos()

        # draw_text("(x="+str(round(mx/w,4))+", y="+str(round(my/h,4))+")",
        # medium_font, black, screen, 0.3*w,0,0)
        # Useful to see positions when placing things

        # rect = pygame.Rect(0.65*w,0.23*h,int(w*0.3),int(w*0.3))
        # pygame.draw.rect(screen, green, rect)
        # In order to see the place where the plant image is displayed
        # Keep that uncomment please

        list_of_events = pygame.event.get()

        mxw = mx / w

        if a <= mxw and mxw <= b and my / h > 0.2:

            abscisses = int((mxw - a) / (b - a) * 1080)

            # draw_text("abscisses="+str(abscisses), medium_font, black, screen, 0.8*w,0.1*h,0)
            # Keep also that please

            if 0 <= abscisses <= len(data):
                species_name = str(data.species_name[abscisses])
                draw_text(
                    "Species : " + species_name,
                    font,
                    black,
                    screen,
                    0.65 * w,
                    0.78 * h,
                    0,
                )

                images = int(data.Images[abscisses])
                draw_text(
                    "Number of Images : " + str(images),
                    font,
                    black,
                    screen,
                    0.65 * w,
                    0.82 * h,
                    0,
                )

                id_species = data.id_species[abscisses]
                path_to_DIR = os.path.join(path_to_train, str(id_species))
                os.chdir(path_to_DIR)

                number_images = len(
                    os.listdir()
                )  # first part of gadget to change the plant photo with right click
                if plant_representative > number_images - 1:
                    plant_representative = 0

                if number_images > 0:  # Display of the photo of the plant-species
                    # print(len(os.listdir()))
                    plant_image_jpg_name = os.listdir()[plant_representative]
                    plant_image = pygame.image.load(
                        os.path.join(path_to_DIR, plant_image_jpg_name)
                    )
                    plant_image = pygame.transform.scale(
                        plant_image, (int(w * 0.3), int(w * 0.3))
                    )
                    screen.blit(plant_image, (0.65 * w, 0.23 * h))

                for (
                    event
                ) in (
                    list_of_events
                ):  # second part of the gadget to change the plant representative with right click
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 3:
                            plant_representative += 1

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

