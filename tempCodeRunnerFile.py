
# def Images():
#     running = True
#     while running:
#         screen.fill(white)
#         arrow_button = pygame.Rect(0.9*w,0, w*0.1 , h*0.1)

#         screen.blit(images_repartition,(0.06*w,0.1*h))

#         mx, my = pygame.mouse.get_pos()
#         draw_text("(x="+str(mx)+", y="+str(my)+")", font, black, screen, 0,0.6*h)
#         draw_text("(x="+str(round(mx/w,2))+", y="+str(round(my/h,2))+")", font, black, screen, 0,0.7*h)

#         if 160<=mx<=830:
#             abscisses=int(((mx-160)/(830-160))*1080)
#             draw_text("abscisses="+str(abscisses), font, black, screen, 0.5*w,0.5*h)
#             if 0<=abscisses<=1080:
#                 species_name = data.species_name[abscisses]
#                 draw_text(species_name, font, black, screen, 0.5*w,0.65*h)

#                 images = data.Images[abscisses]
#                 draw_text("Number of Images : "+str(images), font, black, screen, 0.5*w,0.55*h)

#                 id_species = data.id_species[abscisses]
#                 path_to_DIR = os.path.join(path_to_train,str(id_species))
#                 os.chdir(path_to_DIR)
#                 if len(os.listdir())>0:
#                     plant_image_jpg_name = os.listdir()[0]
#                     plant_image = pygame.image.load(os.path.join(path_to_DIR,plant_image_jpg_name))
#                     plant_image = pygame.transform.scale(plant_image, (int(w*0.3),int(h*0.3)))
#                     screen.blit(plant_image,(0.65*w,0.2*h))

#         # draw_text('Number of images for each species', font, black, screen, 20, 20)

#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == KEYDOWN:
#                 if event.key == K_ESCAPE:
#                     running = False
#             if arrow_button.collidepoint((mx, my)):
#                 if event.type == MOUSEBUTTONDOWN:
#                     running = False
#         if arrow_button.collidepoint((mx, my)):
#             screen.blit(arrow_back_grey,(0.9*w,0))
#         else :
#             screen.blit(arrow_back,(0.9*w,0))

#         pygame.display.update()
#         mainClock.tick(60)

# #### End of Number of images for each species ###