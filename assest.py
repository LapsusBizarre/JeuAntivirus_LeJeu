import pygame
import math

screen = pygame.display.set_mode((960,600))

#importer de charger l'arriere plan de notre jeu
background=pygame.image.load('PygameAssets-Jeu_AntiVirus/download.jpg')

#importer charger notre banniere
banner = pygame.image.load('PygameAssets-Jeu_AntiVirus/sglLogo.png')
banner = pygame.transform.scale(banner, (116, 175))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/2.25)
#banner_rect.y = math.ceil(screen.get_width()/2)

#import charger notre bouton pour lancer la partie
#image du bouton Starter
play_button = pygame.image.load('PygameAssets-Jeu_AntiVirus/Startbutton.png')
play_button = pygame.transform.scale(play_button, (272, 61))
play_button_rect = play_button.get_rect()
play_button_rect.topleft = (200, 300)

#Import charger nos boutons pour choisir le niveaux
#image du bouton Junior
Junior_button = pygame.image.load('PygameAssets-Jeu_AntiVirus/Junior_button.png')
Junior_button = pygame.transform.scale(Junior_button, (275, 60))
Junior_button_rect = Junior_button.get_rect()
Junior_button_rect.x = math.ceil(screen.get_width()/2)
Junior_button_rect.topleft = (500, 300)

#image du bouton Master
Master_button = pygame.image.load('PygameAssets-Jeu_AntiVirus/Master_button.png')
Master_button = pygame.transform.scale(Master_button, (272, 60))
Master_button_rect = Master_button.get_rect()
Master_button_rect.topleft = (200, 200)

#image du bouton Expert
Expert_button = pygame.image.load('PygameAssets-Jeu_AntiVirus/Expert_button.png')
Expert_button = pygame.transform.scale(Expert_button, (272, 60))
Expert_button_rect = Expert_button.get_rect()
Expert_button_rect.topleft = (500, 200)