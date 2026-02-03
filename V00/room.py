#Description du fichier : VOO/room.py
#Ce fichier contient les pièces ue le joueur peut visiter dans le jeu textuel .

# Definition de la classe Room
class Room :
    def __init__(self, name, description):
        """
        Initialise une nouvelle pièce du jeu.

        Args :
            name (str) : Le nom de la pièce.
            description (str) : La description de la pièce.
        """
        self.name = name
        self.description = description
        self.exits = {} # Dictionnaire des sorties de la pièce
        self.items = [] # Liste des objets dans la pièce
    
    def add_exit(self, direction, room):
        """
        Ajoute une sortie à la pièce.

        Args :
            direction (str) : La direction de la sortie (N, S, E, O).
            room (Room) : La pièce vers laquelle la sortie mène.
        """
        self.exits[direction] = room
    
    def get_exit(self, direction):
        """
        Retourne la pièce associée à une direction.
        """
        return self.exits.get(direction)
    
    def describe(self):
        """
        Affiche la description de la pièce et ses sorties disponibles.
        """
        print(self.description)
        if self.exits:
            print("Sorties disponibles : " + ", ".join(self.exits.keys()))
        else:   
            print("Aucune sortie disponible.")
        if self.items:
            print("Objets visibles : " + ", ".join([item.name for item in self.items]))

    