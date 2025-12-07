#Import des pages externe

import pygame
import game
import assest

import time

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
        assest.screen.blit(assest.background_intro, (0, 0))
        assest.screen.blit(assest.banner, assest.banner_rect)  # si je veux superposer des images, je mets mon code de l'image qui est en dessous avant celui qui est au dessus
        assest.screen.blit(assest.play_button, (125, 425))
        assest.screen.blit(assest.Junior_button, (125, 275))
        assest.screen.blit(assest.Master_button, (575, 425))
        assest.screen.blit(assest.Expert_button, (575, 275))
        assest.screen.blit(assest.Cercle,(320, 200))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                # vérification pour savoir si la souris est en collision avec le bouton jouer
                    # mettre le jeu en mode "lancé"
                if assest.play_button_rect.collidepoint(event.pos):
                    game.choix_level(1)

                elif assest.Junior_button_rect.collidepoint(event.pos):
                    game.choix_level(2)

                elif assest.Expert_button_rect.collidepoint(event.pos):
                    game.choix_level(3)

                elif assest.Master_button_rect.collidepoint(event.pos):
                    game.choix_level(4)


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
        for keys, value in game.virus_coordonne.items() :
            keys_retravailler = str(pygame.key.name(keys))[1]
            texte =value + " : Press " + keys_retravailler
            color = (0,0,0)
            font = pygame.font.SysFont('Segoe UI', 24)
            if value == game.virus_clique :
                color = (255,0,0)
            position_atome = font.render(str(texte) , False, color)
            y = y +40
            screen.blit(position_atome, (770, y))


        #appliquer l'image des different element

        for element in game.list_virus:
            joueur = getattr(game, element[0])
            screen.blit(joueur.image, joueur.rect) #player.rect est le déplacement

        #mettre à jour l'écran
        pygame.display.flip()

        for event in pygame.event.get():
            # Action pour l'event "Fermeture du Jeu"
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")

            # détecte si un joueur lâche une touche du clavier

            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                for element in game.bouton_utilisable.keys():
                    if keys[element]:
                        game.joueur_clique = game.bouton_utilisable[element]
                        game.virus_clique = game.virus_coordonne[element]

                if event.key == pygame.K_RIGHT and (game.joueur_clique.rect.x< 740 - game.joueur_clique.bottom_x  and game.joueur_clique.rect.y > 39) :
                    if game.verification_positions_atomes(game.virus_clique, True, False):
                        game.joueur_clique.move_right()
                        nb_mouvement += 1
                elif event.key == pygame.K_LEFT  and (game.joueur_clique.rect.x > 215 and game.joueur_clique.rect.y< 562 - game.joueur_clique.bottom_y) :
                    if game.verification_positions_atomes(game.virus_clique, False, True):
                        game.joueur_clique.move_left()
                        nb_mouvement += 1
                elif event.key == pygame.K_UP and (game.joueur_clique.rect.x > 216 and game.joueur_clique.rect.y  > 39 ) :
                    if game.verification_positions_atomes(game.virus_clique, False, False):
                        game.joueur_clique.move_up()
                        nb_mouvement += 1
                elif event.key == pygame.K_DOWN and ( game.joueur_clique.rect.x < 740 - game.joueur_clique.bottom_x and game.joueur_clique.rect.y < 562 -game.joueur_clique.bottom_y) :
                    if game.verification_positions_atomes(game.virus_clique, True, True):
                        game.joueur_clique.move_down()
                        nb_mouvement += 1


                # Permet l'initalisation du debut - PROBLEME : le systeme de niveau n'est pas implementé