import pygame
class Player(pygame.sprite.Sprite):

    def __init__(self, name):

        # Fait appelle à la classe Pygame
        super().__init__()

        # Permet d'initialiser pour chaque virus demandé
        self.image = pygame.image.load(f'PygameAssets-Jeu_AntiVirus/{name}.PNG')
        self.rect = self.image.get_rect()

        # Permet de définir la taille du déplacement
        self.velocity = 70

        # Permet de définir la position de départ - LE RECT X ET Y NE SONT QUE TEMPORAIRE
        self.rect.x = 692
        self.rect.y = 512

        self.bottom_x = self.rect.bottomright[0] - self.rect.topleft[0]
        self.bottom_y = self.rect.bottomright[1] - self.rect.topleft[1]




    def move_right(self):
        self.rect.x += self.velocity
        self.rect.y -= self.velocity
        print(self.rect.height)
        print(self.rect.h)
        print("___")
        print(self.bottom_x)
        print(self.bottom_y)

    def move_left(self):
        self.rect.y += self.velocity
        self.rect.x -= self.velocity

    def move_up(self):
        self.rect.x -= self.velocity
        self.rect.y -= self.velocity

    def move_down(self):
        self.rect.x += self.velocity
        self.rect.y += self.velocity