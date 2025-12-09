#Import des pages externe

import pygame
import game
import assest
import math

from threading import Event


pygame.init()
pygame.font.init()

# générer la fenêtre de jeu
pygame.display.set_caption("Anti Virus")
screen = pygame.display.set_mode((960,600))



# MISE EN PLACE DU JEU

#charger notre jeu et defini le level
game = game.Level()
running = True
nb_mouvement = 0

#boucle tant que cette condition est vraie
while running:
    if not game.is_playing :
        assest.Roue_et_Aiguille(game.last_aiguille_angle,game.last_aiguille_tuple)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # vérification pour savoir si la souris est en collision avec le bouton jouer
                    # mettre le jeu en mode "lancé"
                if assest.Start_button_rect.collidepoint(event.pos):
                    game.last_aiguille_angle = 300
                    game.last_aiguille_tuple = (296, 300)
                    assest.Roue_et_Aiguille(300,(296, 300))
                    Event().wait(1.5)
                    game.choix_level(1)

                elif assest.Junior_button_rect.collidepoint(event.pos):
                    game.last_aiguille_angle = 240
                    game.last_aiguille_tuple = (294, 224)
                    assest.Roue_et_Aiguille(240,(294, 224))
                    Event().wait(1.5)
                    game.choix_level(2)

                elif assest.Expert_button_rect.collidepoint(event.pos):
                    game.last_aiguille_angle = 120
                    game.last_aiguille_tuple = (423, 223)
                    assest.Roue_et_Aiguille(120,(423, 223))
                    Event().wait(1.5)
                    game.choix_level(3)

                elif assest.Master_button_rect.collidepoint(event.pos):
                    game.last_aiguille_angle = 60
                    game.last_aiguille_tuple = (425, 297)
                    assest.Roue_et_Aiguille(60,(425, 297))
                    Event().wait(1.5)
                    game.choix_level(4)

            elif event.type == pygame.QUIT:
                running = False
                pygame.quit()

    else:
        #appliquer l'arriere plan de notre jeu
        screen.blit(assest.background, (0, 0))

        # Permet le changement de niveau
        if game.Virus.rect.x <= 215 and game.Virus.rect.y <= 39:
            game.Virus.move_up()
            nb_mouvement = 0
            game.level_complete = True
    
        if game.level_complete:
            game.next_level()
        # Fin de changement de niveau

        # Ecriture du texte sur le coté
        my_font = pygame.font.SysFont('Segoe UI', 40)
        my_font_2 = pygame.font.SysFont('Segoe UI', 25)

        text_mouvement = "Vous avez fait"
        text_mouvement_2 = str(nb_mouvement) + " mouvement(s)"
        mouvement_actuel = my_font_2.render(text_mouvement, False, (0, 0, 0))
        mouvement_actuel_2 = my_font_2.render(text_mouvement_2, False, (0, 0, 0))
        screen.blit(mouvement_actuel, (770, 150))
        screen.blit(mouvement_actuel_2, (770, 175))

        text_level = 'Level ' + str(game.nb_level)
        level_actuel = my_font.render(text_level , False, (0, 0, 0))
        screen.blit(level_actuel, (770, 90))
        y = 190
        for keys, value in game.liste_virus_utilise.items() :
            keys_retravailler = str(pygame.key.name(keys))[1]
            texte =value + " : Press " + keys_retravailler
            color = (0,0,0)
            font = pygame.font.SysFont('Segoe UI', 24)
            if value == game.string_virus_clique :
                color = (255,0,0)
            position_atome = font.render(str(texte) , False, color)
            y = y +40
            screen.blit(position_atome, (770, y))


        #appliquer l'image des different element

        for element in game.list_virus:
            joueur = getattr(game, element[0])
            screen.blit(joueur.image, joueur.rect) #player.rect est le déplacement


        Home_rect, Reload_rect = assest.menu((game.nb_level//game.nombre_de_niveau_par_level)-1) # Formule pour automatiser le changement de couleur

        # mettre à jour l'écran
        pygame.display.flip()

        for event in pygame.event.get():
            # Action pour l'event "Fermeture du Jeu"
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()

            # détecte si un joueur lâche une touche du clavier

            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                for element in game.bouton_utilisable.keys():
                    if keys[element]:
                        game.class_virus_clique = game.bouton_utilisable[element]
                        game.string_virus_clique = game.liste_virus_utilise[element]

                if event.key == pygame.K_RIGHT and (game.class_virus_clique.rect.x < 740 - game.class_virus_clique.bottom_x and game.class_virus_clique.rect.y > 39) :
                    if game.verification_positions_atomes(game.string_virus_clique, True, False):
                        game.class_virus_clique.move_right()
                        nb_mouvement += 1
                elif event.key == pygame.K_LEFT  and (game.class_virus_clique.rect.x > 215 and game.class_virus_clique.rect.y < 562 - game.class_virus_clique.bottom_y) :
                    if game.verification_positions_atomes(game.string_virus_clique, False, True):
                        game.class_virus_clique.move_left()
                        nb_mouvement += 1
                elif event.key == pygame.K_UP and (game.class_virus_clique.rect.x > 216 and game.class_virus_clique.rect.y > 39) :
                    if game.verification_positions_atomes(game.string_virus_clique, False, False):
                        game.class_virus_clique.move_up()
                        nb_mouvement += 1
                elif event.key == pygame.K_DOWN and (game.class_virus_clique.rect.x < 740 - game.class_virus_clique.bottom_x and game.class_virus_clique.rect.y < 562 - game.class_virus_clique.bottom_y) :
                    if game.verification_positions_atomes(game.string_virus_clique, True, True):
                        game.class_virus_clique.move_down()
                        nb_mouvement += 1



            elif event.type == pygame.MOUSEBUTTONDOWN:
                if Home_rect.collidepoint(event.pos):
                    game.is_playing = False
                elif Reload_rect.collidepoint(event.pos):
                    game.choix_level(game.nb_level)
                    nb_mouvement = 0
