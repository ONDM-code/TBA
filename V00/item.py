# Definition de la classe Item (Objet)
class Item:
    def __init__(self, name, description):
        """
        Initialise un nouvel objet.

        Args :
            name (str) : Le nom de l'objet.
            description (str) : La description de l'objet.
        """
        self.name = name
        self.description = description
    
    def __str__(self):
        """
        Retourne une représentation textuelle de l'objet.
        """
        return f"{self.name}: {self.description}"

# Il peut aussi avoir un poids et interagir avec le monde ( TBA et/ou le joueur ) 
# 1. Ajouter des objets inerte ( livre , chaise ...)
# 2. Ajouter des objets interactif ( potion de soin , arme ... )