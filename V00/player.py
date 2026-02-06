# Definition de la Class du joueur
class Player :

    #Definition du constructeur
    def __init__(self, name):
        """
        Initialise un nouveau joueur.

        Args :
            name (str) : Le nom du joueur.
        """
        self.name = name
        self.current_room = None  # La pièce actuelle du joueur
        self.previous_room = None  # La pièce précédente du joueur
        self.inventory = []  # Inventaire du joueur

    #Definition de la méthode pour déplacer le joueur
    def move(self, direction):
        """
        Déplace le joueur dans la direction spécifiée si possible.

        Args :
            direction (str) : La direction dans laquelle le joueur veut se déplacer (N, S, E, O).

        Returns :
            bool : True si le déplacement a réussi, False sinon.
        """
        next_room = self.current_room.get_exit(direction)
        if next_room is None:
            print("\nVous ne pouvez pas aller dans cette direction.\n")
            return False
        
        #Déplacer le joueur vers la pièce suivante
        if next_room:
            self.previous_room = self.current_room
            self.current_room = next_room
            self.current_room.describe()
        return True