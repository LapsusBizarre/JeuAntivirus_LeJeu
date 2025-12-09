import Player

class Level:

#liste des virus possible :  Virus ,Blue_2,Orange_3,Pink_2,Green_2,Blue_3,Purple_3,Green_3,Yellow_3

    def __init__(self):

        # Le booléen permet de différencier si l'utilisateur doit être sur une session "acceuil" ou "en jeux"
        self.is_playing = False


        self.bouton_utilisable = {}  # Liste les boutons qui seront utilisés dans le niveau selectioné
        self.coordonnes_fixes_des_atomes = {} # Recupere la position des differents atomes dans l'image des atomes
        self.liste_virus_utilise = {} # Liste le nom en string du virus du niveau utilisé
        self.string_virus_clique = "Virus"

        # Ensemble des caractéristiques de l'aiguille sur l'ecran d'acceuil
        self.last_aiguille_angle = 300
        self.last_aiguille_tuple = (296, 300)

        self.list_virus = [] # Initialisation de la liste avec les détails du niveau
        # Liste des niveaux disponibles, le niveau 0 existant pour eviter les erreurs
        self.list_level = [self.ecran_dacceuil,
                           self.niveau_facile_1,
                           self.niveau_facile_2,
                           self.niveau_facile_3,
                           self.niveau_facile_4]
        self.nb_level = -1
        self.nombre_de_niveau_par_level = 1 # Nombre de niveau par "Level"
        self.next_level()
        self.level_complete = False
        self.class_virus_clique = None

# Permet la création de la liste qui sert à indiquer la liste des atomes bougeables
    def creation_liste_numpad_virus(self): # Permet de définir les touches "autorisées" pour bouger les players existants
        bouton = {}
        for element in self.list_virus:
            if element[0] == "Virus":
                bouton[1073741922]=self.Virus
            elif element[0] == "Virus":
                bouton[48] = self.Virus

            elif element[0] == "Blue_2":
                bouton[1073741913]=self.Blue_2
            elif element[0] == "Blue_2":
                bouton[49]=self.Blue_2

            elif element[0] == "Orange_3":
                bouton[1073741914]=self.Orange_3
            elif element[0] == "Orange_3":
                bouton[50] = self.Orange_3

            elif element[0] == "Pink_2":
                bouton[1073741915]=self.Pink_2
            elif element[0] == "Pink_2":
                bouton[51]=self.Pink_2

            elif element[0] == "Green_2":
                bouton[1073741916]=self.Green_2
            elif element[0] == "Green_2":
                bouton[52]=self.Green_2

            elif element[0] == "Blue_3":
                bouton[1073741917]=self.Blue_3
            elif element[0] == "Blue_3":
                bouton[53]=self.Blue_3

            elif element[0] == "Purple_3":
                bouton[1073741918]=self.Purple_3
            elif element[0] == "Purple_3":
                bouton[54]=self.Purple_3

            elif element[0] == "Green_3":
                bouton[1073741919]=self.Green_3
            elif element[0] == "Green_3":
                bouton[55]=self.Green_3

            elif element[0] == "Yellow_3":
                bouton[1073741920]=self.Yellow_3
            elif element[0] == "Yellow_3":
                bouton[56]=self.Yellow_3
        return bouton

# Permet la création de la liste qui sert à indiquer les atomes present afin de gerer les collisions
    def creation_liste_collision_virus(self):
        virus_collision = {}
        for element in self.list_virus:
            if element[0] == "Virus":
                virus_collision[1073741922] = "Virus"
            elif element[0] == "Blue_2":
                virus_collision[1073741913] = "Blue_2"
            elif element[0] == "Orange_3":
                virus_collision[1073741914] = "Orange_3"
            elif element[0] == "Pink_2":
                virus_collision[1073741915] = "Pink_2"
            elif element[0] == "Green_2":
                virus_collision[1073741916] = "Green_2"
            elif element[0] == "Blue_3":
                virus_collision[1073741917] = "Blue_3"
            elif element[0] == "Purple_3":
                virus_collision[1073741918] = "Purple_3"
            elif element[0] == "Green_3":
                virus_collision[1073741919] = "Green_3"
            elif element[0] == "Yellow_3":
                virus_collision[1073741920] = "Yellow_3"
        return virus_collision

# Permet l'assignation des differents atomes qui vont apparaitre, leurs positions, et leur touche assignée
    def creation_virus(self):
        self.coordonnes_fixes_des_atomes = {}
        for name in self.list_virus:
            if name[2] != 0:
                setattr(self, name[0], getattr(Player, name[0])(name[2]))
            else:
                setattr(self, name[0], getattr(Player, name[0])())

            getattr(self, name[0]).rect.x += 140*name[1]["x"]
            getattr(self, name[0]).rect.y += 140*name[1]["y"]

            self.coordonnes_fixes_des_atomes[name[0]] = [(getattr(self, name[0]).Ax, getattr(self, name[0]).Ay),
                                                         (getattr(self, name[0]).Bx,getattr(self, name[0]).By),
                                                         (getattr(self, name[0]).Cx,getattr(self, name[0]).Cy)]

        self.bouton_utilisable = self.creation_liste_numpad_virus() # Permet d'assigner à un dictionnaire le lien touche/Nom de l'atome
        self.liste_virus_utilise = self.creation_liste_collision_virus() # Permet d'assigner à un dictionnaire le lien touche/Classe de l'atome

# Permet de vérifier la position de tous les atomes presents
    def verification_positions_atomes(self, virus, hautx:bool, hauty:bool):

        virus_position_list = self.coordonnes_fixes_des_atomes.copy() #Recupere l'ensemble des coordonnées fixes sous la forme de dictionnaire
        virus_actuelle = virus_position_list.pop(virus) # Recuperer les valeurs du virus recherché et sépare en deux entités différentes l'atome selectionné et l'ensemble des autres virus

        coordonne_virus = []
        coordonne_autre = []

        for i in range(0,3):
            if virus_actuelle[i][0] is not None or virus_actuelle[i][1] is not None :
                coordonne_virus.append(((getattr(self,virus).rect.x + virus_actuelle[i][0],
                                         getattr(self,virus).rect.y + virus_actuelle[i][1]))) #Recuperer le pixel (1,1) de l'image du virus et ajoute la position sur de l'atome par rapport à l'image du son virus

        for key, valeur in virus_position_list.items():  # on parcourt les valeurs du dictionnaire pour recuperer les coordonées des autres virus du jeu
            for i in range(0, 3):
                if valeur[i][0] is not None or valeur[i][1] is not None :
                    coordonne_autre.append(((getattr(self,key).rect.x + valeur[i][0],
                                             getattr(self,key).rect.y + valeur[i][1])))#Recuperer le pixel (1,1) de l'image du virus et ajoute la position sur de l'atome par rapport à l'image du son virus

        def systeme_bool(bool:bool,value_origine,value_seconde): #Systeme permettant de vérifier la presence de l'objet en fonction de sa direction en x et en y
            if bool:
                return value_seconde-20 <= value_origine+70 <= value_seconde+20 # Verifie si un atome dans la future nouvelle position (en direction du bas) ne touche pas un atome à plus ou moins 20 pixels près sur l'axe selectionner
            else :
                return value_seconde-20 <= value_origine-70 <= value_seconde+20 # Verifie si un atome dans la future nouvelle position (en direction du haut) ne touche pas un atome à plus ou moins 20 pixels près sur l'axe séléctionner

        for i in coordonne_virus:
            for j in coordonne_autre:
                if systeme_bool(hautx,i[0],j[0]) and systeme_bool(hauty,i[1],j[1]):
                    return False
        return True # return True si pas de problème ou False si un atome est là

# Permet le systeme de selection des niveaux
    def choix_level(self,valeur):
        self.nb_level = (valeur-1)
        self.next_level()
        self.is_playing = True

# Permet d'automatiser le changement de niveau
    def next_level(self):
        try :
            self.nb_level += 1
            self.list_level[self.nb_level]()
            self.level_complete = False
            self.class_virus_clique = self.Virus
        except IndexError :
            self.is_playing = False



# LES NIVEAUX : Le format [[Nom_de_l'atome_1 , {"x" : position en x*70, "y" : position en y*70}, angle de rotation], etc]

    def ecran_dacceuil(self):
        self.list_virus = [["Virus",{"x":2 , "y":0},0],
                           ["Pink_2", {"x": 2, "y": 1}, 90]]
        self.creation_virus()

    def niveau_facile_1(self):
        self.list_virus = [["Virus", {"x": 1, "y": 1}, 0],
                           ["Collision",{"x": 2, "y": 2} , 0],
                           ["Purple_3", {"x": 0.5, "y": 0.5}, 180]]
        self.creation_virus()


    def niveau_facile_2(self):
        self.list_virus = [["Virus",{"x":2.5 , "y":1.5},0],
                           ["Yellow_3", {"x": 2, "y": 1}, 0],
                           ["Collision",{"x": 1, "y": 3} , 0],
                           ["Collision_2",{"x": 0.5, "y": 1.5} , 0]]
        self.creation_virus()

    def niveau_facile_3(self):
        self.list_virus = [["Virus", {"x": 0, "y": 2}, 0],
                           ["Pink_2", {"x": 2, "y": 1}, 90],
                           ["Blue_2", {"x": 2.5, "y": 2.5}, 270],
                           ["Collision", {"x": 0.5, "y": 1.5}, 0],
                           ["Collision_2", {"x": 1.5, "y": 1.5}, 0]]
        self.creation_virus()

    def niveau_facile_4(self):
        self.list_virus = [["Blue_3", {"x": 0, "y": 0}, 0],
                           ["Purple_3", {"x": 1, "y": 1}, 90],
                           ["Collision", {"x": 2.5, "y": 1.5}, 0],
                           ["Virus", {"x": 0.5, "y": 2.5}, 0]]
        self.creation_virus()