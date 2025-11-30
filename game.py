import Player

class Level:

#liste des virus possible :  Virus ,Blue_2,Orange_3,Pink_2,Green_2,Blue_3,Purple_3,Green_3,Yellow_3]

    def __init__(self):
        self.is_playing = False

        self.list_virus = []
        self.list_level = [self.ecran_dacceuil,self.niveau_facile]
        self.bouton_utilisable = {}

        self.nb_level = -1
        self.next_level()
        self.level_complete = False
        self.joueur_clique = self.Virus

    def valeur_virus(self): # Permet de définir les touches "autorisées" pour bouger les players existants
        bouton = {}
        for element in self.list_virus:
            if element[0] == "Virus":
                bouton[1073741922]=self.Virus
            elif element == "Blue_2":
                bouton[1073741913]=self.Blue_2
            elif element == "Orange_3":
                bouton[1073741914]=self.Orange_3
            elif element == "pink_2":
                bouton[1073741915]=self.pink_2
            elif element == "green_2":
                bouton[1073741916]=self.green_2
            elif element == "blue_3":
                bouton[1073741917]=self.blue_3
            elif element[0] == "Purple_3":
                bouton[1073741918]=self.Purple_3
            elif element == "green_3":
                bouton[1073741919]=self.green_3
            elif element == "yellow_3":
                bouton[1073741920]=self.yellow_3
        return bouton

    def next_level(self):
        self.nb_level += 1
        self.list_level[self.nb_level]()
        self.level_complete = False
        self.joueur_clique = self.Virus


    def creation_virus(self):
        for name in self.list_virus:
            setattr(self, name[0], getattr(Player, name[0])())
            getattr(self, name[0]).rect.x += 70*name[1]["x"]
            getattr(self, name[0]).rect.y += 70*name[1]["y"]
        self.bouton_utilisable = self.valeur_virus()

    def ecran_dacceuil(self):
        self.list_virus = [["Virus",{"x":4 , "y":6}]]
        self.creation_virus()

    def niveau_facile(self):
        self.list_virus = [["Virus", {"x": 2, "y": 2}],
                           ["Purple_3", {"x": 3, "y": 3}]]
        self.creation_virus()

    def niveau_moyen(self):
        self.list_virus = []
        self.creation_virus()