import pygame
import assest

def main():
    # vérifier si notre n'a pas commencé
    # ajouter mon écran de bienvenue
    assest.screen.blit(assest.banner,
                assest.banner_rect)  # si je veux superposer des images, je met mon code de l'image qui est en dessous avant celui qui est au dessus
    assest.screen.blit(assest.play_button, (200, 300))
    assest.screen.blit(assest.Junior_button, (500, 300))
    assest.screen.blit(assest.Master_button, (200, 200))
    assest.screen.blit(assest.Expert_button, (500, 200))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            #vérification pour savoir si la souris est en collision avec le bouton jouer
            if assest.play_button_rect.collidepoint(event.pos) or assest.Junior_button_rect.collidepoint(event.pos) or assest.Master_button_rect.collidepoint(event.pos) or assest.Expert_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode "lancé"
                return True
            else :
                return False