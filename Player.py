import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, name):

        # Fait appelle à la classe Pygame
        super().__init__()
        # Permet d'initialiser pour chaque virus demandé
        self.image = pygame.image.load(f'PygameAssets-Jeu_AntiVirus/{name}.png')
        self.rect = self.image.get_rect()

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

        super().__init__("Virus")

        self.Ax = 51
        self.Ay = 51
        self.Bx = 125
        self.By = 125
        self.Cx = None
        self.Cy = None

        self.rect.x -= self.Ax
        self.rect.y -= self.Ay

class Blue_2(Player):

    def __init__(self,rotate):
        super().__init__("blue_2")
        self.image = pygame.transform.rotate(self.image, rotate)
        if rotate == 270:
            self.Ax = 50
            self.Ay = 120
            self.Bx = 120
            self.By = 50
        else :
            self.Ax = 51
            self.Ay = 51
            self.Bx = 125
            self.By = 125

        self.Cx = None
        self.Cy = None
        self.rect.x -= self.Ax
        self.rect.y -= self.Ay


class Collision(Player):

    def __init__(self):
        super().__init__("collision")
        self.Ax = 50
        self.Ay = 47
        self.Bx = None
        self.By = None
        self.Cx = None
        self.Cy = None
        self.rect.x -= self.Ax
        self.rect.y -= self.Ay

class Collision_2(Collision):
    def __init__(self):
        super().__init__()

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

class Pink_2(Player):

    def __init__(self,rotate=0):
        super().__init__("Pink_2")
        self.image = pygame.transform.rotate(self.image, rotate)
        if rotate == 90:
            self.Ax = 51
            self.Ay = 51
            self.Bx = 51
            self.By = 195

            z = self.bottom_x
            self.bottom_x = self.bottom_y
            self.bottom_y = z
        else:
            self.Ax = 51
            self.Ay = 51
            self.Bx = 195
            self.By = 51
        self.Cx = None
        self.Cy = None
        self.rect.x -= self.Ax
        self.rect.y -= self.Ay

class Green_2(Player):

    def __init__(self):
        super().__init__("green_2")
        self.Ax = 51
        self.Ay = 51
        self.Bx = 203
        self.By = 51
        self.Cx = None
        self.Cy = None
        self.rect.x -= self.Ax

class Blue_3(Player):
    def __init__(self):
        super().__init__("blue_3")
        self.Ax = 51
        self.Ay = 51
        self.Bx = 203
        self.By = 51
        self.Cx = 350
        self.Cy = 51
        self.rect.x -= self.Ax
        self.rect.y -= self.Ay

class Purple_3(Player):
    def __init__(self,rotate=0):
        super().__init__("purple_3")
        self.image = pygame.transform.rotate(self.image, rotate)
        self.Ax = 195
        self.Ay = 51

        if rotate == 180:
            self.Bx = 53
            self.By = 51
            self.Cx = 53
            self.Cy = 199
            self.rect.x -= self.Bx
            self.rect.y -= self.By
        elif rotate == 90:
            self.Bx = 201
            self.By = 199
            self.Cx = 53
            self.Cy = 51
            self.rect.x -= self.Cx
            self.rect.y -= self.Cy
        else :
            self.Bx = 201
            self.By = 199
            self.Cx = 53
            self.Cy = 199
            self.rect.x -= self.Ax
            self.rect.y -= self.Ay



class Green_3(Player):
    def __init__(self,rotate=0):
        super().__init__("green_3")
        self.image = pygame.transform.rotate(self.image, rotate)
        self.Ax = 50
        self.Ay = 50
        self.Bx = 120
        self.By = 120
        self.Cx = 120
        self.Cy = 273
        self.rect.x -= self.Ax
        self.rect.y -= self.Ay

class Yellow_3(Player):
    def __init__(self, rotate=0):
        super().__init__("yellow_3")
        self.image = pygame.transform.rotate(self.image, rotate)
        self.Ax = 51
        self.Ay = 124
        self.Bx = 51
        self.By = 273
        self.Cx = 126
        self.Cy = 51
        self.rect.x -= self.Ax
        self.rect.y -= self.Ay