import pygame
class Player(pygame.sprite.Sprite):

    def __init__(self, name):

        # Fait appelle à la classe Pygame
        super().__init__()
        # Permet d'initialiser pour chaque virus demandé
        self.image = pygame.image.load(f'PygameAssets-Jeu_AntiVirus/{name}.PNG')
        self.rect = self.image.get_rect()
        print(self.image)

        # Permet de définir la taille du déplacement
        self.velocity = 70

        # Permet de définir la position de départ
        self.rect.x = 266
        self.rect.y = 88

        self.bottom_x = self.rect.bottomright[0] - self.rect.topleft[0]
        self.bottom_y = self.rect.bottomright[1] - self.rect.topleft[1]



    def move_right(self):
        self.rect.x += self.velocity
        self.rect.y -= self.velocity

    def move_left(self):
        self.rect.y += self.velocity
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.x -= self.velocity
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.x += self.velocity
        self.rect.y += self.velocity

class Virus(Player):
    def __init__(self):

        super().__init__("virus")

        self.Ax = 51
        self.Ay = 51
        self.Bx = 125
        self.By = 125
        self.Cx = None
        self.Cy = None

        self.rect.x -= self.Ax
        self.rect.y -= self.Ay

class Blue_2(Player):

    def __init__(self):
        super().__init__("blue_2")
        self.Ax = 51
        self.Ay = 51
        self.Bx = 125
        self.By = 125
        self.Cx = None
        self.Cy = None
        self.rect.x -= self.Ax
        self.rect.y -= self.Ay

class Orange_3(Player):
    def __init__(self):
        super().__init__("orange_3")
        self.Ax = 51
        self.Ay = 51
        self.Bx = 126
        self.By = 126
        self.Cx = 200
        self.Cy = 50
        self.rect.x -= self.Ax
        self.rect.y -= self.Ay

class Purple_3(Player):
    def __init__(self):
        super().__init__("purple_3")
        self.Ax = 195
        self.Ay = 51
        self.Bx = 201
        self.By = 199
        self.Cx = 53
        self.Cy = 199
        self.rect.x -= self.Ax
        self.rect.y -= self.Ay