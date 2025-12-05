import Player
import pygame

class Level:

#liste des virus possible :  Virus ,Blue_2,Orange_3,Pink_2,Green_2,Blue_3,Purple_3,Green_3,Yellow_3]

    def __init__(self):
        self.is_playing = False

        self.list_virus = []
        self.list_level = [self.ecran_dacceuil,self.niveau_facile,self.niveau_moyen]
        self.bouton_utilisable = {}

        self.coordonne = {}
        self.virus_coordonne = {}
        self.virus_clique = "Virus"

        self.nb_level = -1
        self.next_level()
        self.level_complete = False
        self.joueur_clique = self.Virus

    def valeur_virus(self): # Permet de définir les touches "autorisées" pour bouger les players existants
        bouton = {}
        for element in self.list_virus:
            if element[0] == "Virus":
                bouton[1073741922]=self.Virus
            elif element[0] == "Blue_2":
                bouton[1073741913]=self.Blue_2
            elif element[0] == "Orange_3":
                bouton[1073741914]=self.Orange_3
            elif element[0] == "pink_2":
                bouton[1073741915]=self.pink_2
            elif element[0] == "green_2":
                bouton[1073741916]=self.green_2
            elif element[0] == "blue_3":
                bouton[1073741917]=self.blue_3
            elif element[0] == "Purple_3":
                bouton[1073741918]=self.Purple_3
            elif element[0] == "green_3":
                bouton[1073741919]=self.green_3
            elif element[0] == "yellow_3":
                bouton[1073741920]=self.yellow_3
        return bouton

    def colisition_virus(self):
        virus_colision = {}
        for element in self.list_virus:
            if element[0] == "Virus":
                virus_colision[1073741922] = "Virus"
            elif element[0] == "Blue_2":
                virus_colision[1073741913] = "Blue_2"
            elif element[0] == "Orange_3":
                virus_colision[1073741914] = "Orange_3"
            elif element[0] == "pink_2":
                virus_colision[1073741915] = "Pink_2"
            elif element[0] == "green_2":
                virus_colision[1073741916] = "Green_2"
            elif element[0] == "blue_3":
                virus_colision[1073741917] = "Blue_3"
            elif element[0] == "Purple_3":
                virus_colision[1073741918] = "Purple_3"
            elif element[0] == "green_3":
                virus_colision[1073741919] = "Green_3"
            elif element[0] == "yellow_3":
                virus_colision[1073741920] = "Yellow_3"
        return virus_colision

    def choix_level(self,valeur):
        self.nb_level = (valeur-1)
        self.next_level()
        self.is_playing = True

    def next_level(self):
        try :
            self.nb_level += 1
            self.list_level[self.nb_level]()
            self.level_complete = False
            self.joueur_clique = self.Virus
        except IndexError :
            pygame.font.init()
            my_font = pygame.font.SysFont('Comic Sans MS', 30)
            text_surface = my_font.render('Merci d\'avoir jouer au jeu', False, (255, 255, 255))
            screen = pygame.display.set_mode((960,600))
            screen.blit(text_surface, (300, 300))
            self.is_playing = False


    def creation_virus(self):
        self.coordonne = {}
        for name in self.list_virus:
            if name[2] != 0:
                setattr(self, name[0], getattr(Player, name[0])(name[2]))
            else:
                setattr(self, name[0], getattr(Player, name[0])())

            getattr(self, name[0]).rect.x += 140*name[1]["x"]
            getattr(self, name[0]).rect.y += 140*name[1]["y"]

            self.coordonne[name[0]] = [(getattr(self, name[0]).Ax,getattr(self, name[0]).Ay),
                               (getattr(self, name[0]).Bx,getattr(self, name[0]).By),
                               (getattr(self, name[0]).Cx,getattr(self, name[0]).Cy)]

        self.bouton_utilisable = self.valeur_virus()
        self.virus_coordonne = self.colisition_virus()


    def verification(self,virus,hautx:bool,hauty:bool):
        virus_position_list = self.coordonne.copy()
        virus_actuelle = virus_position_list.pop(virus)
        coordonne_virus = []
        coordonne_autre = []
        for i in range(0,3):
            if virus_actuelle[i][0] != None or virus_actuelle[i][1] != None :
                coordonne_virus.append(((getattr(self,virus).rect.x + virus_actuelle[i][0],
                                         getattr(self,virus).rect.y + virus_actuelle[i][1])))
        for key, valeur in virus_position_list.items():  # on parcours les valeurs du dictionnaire
            for i in range(0, 3):
                if valeur[i][0] != None or valeur[i][1] != None :
                    coordonne_autre.append(((getattr(self,key).rect.x + valeur[i][0],
                                             getattr(self,key).rect.y + valeur[i][1])))

        def systeme_bool(bool:bool,value_origine,value_seconde):
            if bool:
                return value_seconde-10 <= value_origine+70 <= value_seconde+10
            else :
                return value_seconde-10 <= value_origine-70 <= value_seconde+10

        for i in coordonne_virus:
            for j in coordonne_autre:
                if systeme_bool(hautx,i[0],j[0]) and systeme_bool(hauty,i[1],j[1]):
                    return False
        return True # return true si pas de probleme or False si un atome est là

    def ecran_dacceuil(self):
        self.list_virus = [["Virus",{"x":2 , "y":0},0]]
        self.creation_virus()

    def niveau_facile(self):
        self.list_virus = [["Virus", {"x": 1, "y": 1}, 0],
                           ["Collision",{"x": 2, "y": 2} , 0],
                           ["Purple_3", {"x": 0.5, "y": 0.5}, 180]]
        self.creation_virus()

    def niveau_moyen(self):
        self.list_virus = [["Virus",{"x":1.5 , "y":1.5},0]]
        self.creation_virus()