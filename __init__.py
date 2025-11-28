#Import des pages externe

import pygame
import game
import PagedAccueil

import time

pygame.init()

# générer la fenêtre de jeu
pygame.display.set_caption("Anti Virus")
screen = pygame.display.set_mode((960,600))



# MISE EN PLACE DU JEU

#charger notre jeu et defini le level
game = game.Level()
joueur_clique = game.Virus
running = True

#boucle tant que cette condition est vraie
while running:

    #appliquer l'arriere plan de notre jeu
    screen.blit(PagedAccueil.background, (0, 0))

    if not game.is_playing:
        # vérifier si notre n'a pas commencé
        # ajouter mon écran de bienvenue
        screen.blit(PagedAccueil.banner,
                    PagedAccueil.banner_rect)  # si je veux superposer des images, je met mon code de l'image qui est en dessous avant celui qui est au dessus
        screen.blit(PagedAccueil.play_button, (200, 300))
        screen.blit(PagedAccueil.Junior_button, (500, 300))
        screen.blit(PagedAccueil.Master_button, (200, 200))
        screen.blit(PagedAccueil.Expert_button, (500, 200))

    # Permet le changement de niveau
    '''
    if game.Virus.rect.x <= 215 and game.Virus.rect.y <= 39:
        game.Virus.move_up()
        game.level_complete = True

    if game.level_complete:
        time.sleep(4)
        game.next_level()
    '''
    # Fin de changement de niveau

    #appliquer l'image des different element
    for element in game.list_virus:
        joueur = getattr(game, element)
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
                    joueur_clique = game.bouton_utilisable[element]

            if event.key == pygame.K_RIGHT and (joueur_clique.rect.x< 740 - joueur_clique.bottom_x  and joueur_clique.rect.y > 39) :
                joueur_clique.move_right()
            elif event.key == pygame.K_LEFT  and (joueur_clique.rect.x > 215 and joueur_clique.rect.y< 562 - joueur_clique.bottom_y) :
                joueur_clique.move_left()
            elif event.key == pygame.K_UP and (joueur_clique.rect.x > 216 and joueur_clique.rect.y  > 39 ) :
                joueur_clique.move_up()
            elif event.key == pygame.K_DOWN and ( joueur_clique.rect.x < 740 - joueur_clique.bottom_x and joueur_clique.rect.y < 562 -joueur_clique.bottom_y) :
                joueur_clique.move_down()



            # Permet l'initalisation du debut - PROBLEME : le systeme de niveau n'est pas implementé

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #vérification pour savoir si la souris est en collision avec le bouton jouer
            if PagedAccueil.play_button_rect.collidepoint(event.pos) or PagedAccueil.Junior_button_rect.collidepoint(event.pos) or PagedAccueil.Master_button_rect.collidepoint(event.pos) or PagedAccueil.Expert_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode "lancé"
                game.is_playing = True
                game.next_level()