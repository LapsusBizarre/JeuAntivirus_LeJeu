#Import des pages externe

import pygame
import game
import PagedAccueil
import assest

import time

pygame.init()

# générer la fenêtre de jeu
pygame.display.set_caption("Anti Virus")
screen = pygame.display.set_mode((960,600))



# MISE EN PLACE DU JEU

#charger notre jeu et defini le level
game = game.Level()
running = True

#boucle tant que cette condition est vraie
while running:
    if not game.is_playing :
        game.is_playing = PagedAccueil.main()

    else:
        #appliquer l'arriere plan de notre jeu
        screen.blit(assest.background, (0, 0))

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

                if event.key == pygame.K_RIGHT and (game.joueur_clique.rect.x< 740 - game.joueur_clique.bottom_x  and game.joueur_clique.rect.y > 39) :
                    game.joueur_clique.move_right()
                elif event.key == pygame.K_LEFT  and (game.joueur_clique.rect.x > 215 and game.joueur_clique.rect.y< 562 - game.joueur_clique.bottom_y) :
                    game.joueur_clique.move_left()
                elif event.key == pygame.K_UP and (game.joueur_clique.rect.x > 216 and game.joueur_clique.rect.y  > 39 ) :
                    game.joueur_clique.move_up()
                elif event.key == pygame.K_DOWN and ( game.joueur_clique.rect.x < 740 - game.joueur_clique.bottom_x and game.joueur_clique.rect.y < 562 -game.joueur_clique.bottom_y) :
                    game.joueur_clique.move_down()


                # Permet l'initalisation du debut - PROBLEME : le systeme de niveau n'est pas implementé