import Player

class Level:

#liste des virus possible :  Virus ,Blue_2,Orange_3,Pink_2,Green_2,Blue_3,Purple_3,Green_3,Yellow_3]

    def __init__(self):
        self.is_playing = False

        self.list_virus = []
        self.list_level = [self.ecran_dacceuil,self.level_1, self.level_2, self.level_3]
        self.bouton_utilisable = {}

        self.nb_level = -1
        self.next_level()
        self.level_complete = False

    def valeur_virus(self): # Permet de définir les touches "autorisées" pour bouger les players existants
        bouton = {}
        for element in self.list_virus:
            if element == "virus":
                bouton[1073741922]=self.virus
            elif element == "blue_2":
                bouton[1073741913]=self.blue_2
            elif element == "orange_3":
                bouton[1073741914]=self.orange_3
            elif element == "pink_2":
                bouton[1073741915]=self.pink_2
            elif element == "green_2":
                bouton[1073741916]=self.green_2
            elif element == "blue_3":
                bouton[1073741917]=self.blue_3
            elif element == "purple_3":
                bouton[1073741918]=self.purple_3
            elif element == "green_3":
                bouton[1073741919]=self.green_3
            elif element == "yellow_3":
                bouton[1073741920]=self.yellow_3
        return bouton

    def creation_virus(self):
        for name in self.list_virus:
            setattr(self, name, Player.Player(name))
        self.bouton_utilisable = self.valeur_virus()


    def next_level(self):
        self.nb_level += 1
        self.list_level[self.nb_level]()
        self.level_complete = False

    def ecran_dacceuil(self):
        self.list_virus = ["virus"]
        self.creation_virus()

    def level_1(self):
        self.list_virus = ["virus","purple_3"]
        self.creation_virus()

    def level_2(self):
        self.list_virus = ["virus","orange_3"]
        self.creation_virus()

    def level_3(self):
        self.list_virus = ["virus","blue_2","orange_3","pink_2", "green_2","blue_3", "purple_3", "green_3", "yellow_3"]
        self.creation_virus()