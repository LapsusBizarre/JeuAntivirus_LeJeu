import pygame

screen = pygame.display.set_mode((960,600))

#importer de charger l'arriere plan de notre jeu
background=pygame.image.load('PygameAssets-Jeu_AntiVirus/download.jpg')

background_intro = pygame.image.load("PygameAssets-Jeu_AntiVirus/bgLevelSelect.jpg")

#importer charger notre banniere
banner = pygame.image.load('PygameAssets-Jeu_AntiVirus/sglLogo.png')
banner = pygame.transform.scale(banner, (120, 160))
banner_rect = banner.get_rect()
banner_rect.bottomright = (960,600)

#import charger notre bouton pour lancer la partie

Fleche_start = pygame.image.load('PygameAssets-Jeu_AntiVirus/Fleche.png')
Fleche_junior = pygame.image.load('PygameAssets-Jeu_AntiVirus/Fleche.png')
Fleche_master = pygame.image.load('PygameAssets-Jeu_AntiVirus/Fleche.png')
Fleche_expert = pygame.image.load('PygameAssets-Jeu_AntiVirus/Fleche.png')

#image du bouton Starter
Start_button = pygame.image.load('PygameAssets-Jeu_AntiVirus/Startbutton.png')
Start_button_rect = Start_button.get_rect()
Start_button_rect.topleft = (125, 400)

#Import charger nos boutons pour choisir le niveaux
#image du bouton Junior
Junior_button = pygame.image.load('PygameAssets-Jeu_AntiVirus/Junior_button.png')
Junior_button_rect = Junior_button.get_rect()
Junior_button_rect.topleft = (125, 275)

#image du bouton Master
Master_button = pygame.image.load('PygameAssets-Jeu_AntiVirus/Master_button.png')
Master_button_rect = Master_button.get_rect()
Master_button_rect.topleft = (575, 400)

#image du bouton Expert
Expert_button = pygame.image.load('PygameAssets-Jeu_AntiVirus/Expert_button.png')
Expert_button_rect = Expert_button.get_rect()
Expert_button_rect.topleft = (575, 275)

Cercle = pygame.image.load('PygameAssets-Jeu_AntiVirus/Cercle.png')

def Roue_et_Aiguille(Aiguille_angle, tuple_position):
    screen.blit(background_intro, (0, 0))
    screen.blit(banner,banner_rect)  # si je veux superposer des images, je mets mon code de l'image qui est en dessous avant celui qui est au dessus
    screen.blit(Start_button, (125, 400))
    screen.blit(Fleche_start, (140, 410))

    screen.blit(Junior_button, (125, 275))
    screen.blit(Fleche_junior, (140, 285))

    screen.blit(Master_button, (575, 400))
    screen.blit(Expert_button, (575, 275))

    screen.blit(Fleche_master, (645, 285))
    screen.blit(Fleche_expert, (645, 410))

    screen.blit(Cercle, (320, 200))

    Aiguille = pygame.image.load('PygameAssets-Jeu_AntiVirus/Aiguille.png')
    Aiguille = pygame.transform.rotate(Aiguille, Aiguille_angle)
    screen.blit(Aiguille, tuple_position)

    pygame.display.flip()

def menu(level_int:int):
    level_list = ["Green", "Orange", "Red", "Blue"]
    Home = pygame.image.load(f'PygameAssets-Jeu_AntiVirus/Home_{level_list[level_int]}.png')
    Home_rect = Home.get_rect()
    Home_rect.topleft = (50, 500)
    screen.blit(Home, (50, 500))

    Reload = pygame.image.load(f'PygameAssets-Jeu_AntiVirus/Reload_{level_list[level_int]}.png')
    Reload_rect = Reload.get_rect()
    Reload_rect.topleft = (50, 430)
    screen.blit(Reload, (50, 430))

    Next = pygame.image.load(f'PygameAssets-Jeu_AntiVirus/Next_{level_list[level_int]}.png')
    Next_rect = Next.get_rect()
    Next_rect.topleft = (50, 360)
    screen.blit(Next, (50, 360))

    return Home_rect, Reload_rect, Next_rect