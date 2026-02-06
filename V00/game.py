# Import modules

from room import Room
from player import Player
from command import Command
from actions import Actions
from item import Item

class Game:
    
#Iniitialisation du jeu
    # Constructeurs
    def __init__(self):
        self.rooms = []
        self.player = None
        self.cmd = {}
        self.finished = False

    # Setup du jeu
    def setup(self):
        

        # Setup des commandes

        go = Command("go",":Aller dans une direction",Actions.go,1)
        self.cmd["go"] = go
        look = Command("look",":Regarder autour de soi",Actions.look,1)
        self.cmd["look"] = look
        help = Command("help",":Afficher de l'aide",Actions.help,0)
        self.cmd["help"] = help
        quit = Command("quit",":Quitter le jeu",Actions.quit,0)
        self.cmd["quit"] = quit
        take = Command("take",":Prendre un objet",Actions.take,1)
        self.cmd["take"] = take
        inventory = Command("inventory",":Afficher l'inventaire",Actions.inventory,0)
        self.cmd["inventory"] = inventory
        back = Command("back",":Revenir à la pièce précédente",Actions.back,0)
        self.cmd["back"] = back
        use = Command("use",":Utiliser un objet",Actions.use,1)
        self.cmd["use"] = use


        # Setup des pièces

        appart = Room( "Appartement d’Axel", "Un petit appartement sombre rempli d’écrans et de câbles. " "C’est ici que commence l’aventure.")
        self.rooms.append(appart)
        rue = Room( "Rue Basse", "Une rue étroite éclairée par des néons. " "Des drones de surveillance patrouillent lentement.")
        self.rooms.append(rue)
        marche_noir = Room( "Marché Noir", "Un lieu clandestin où les informations circulent librement.")
        self.rooms.append(marche_noir)
        serveur = Room( "Serveur Abandonné", "Une ancienne salle de serveurs poussiéreuse. " "Des données oubliées y sont encore stockées.")
        self.rooms.append(serveur)
        ruelles = Room( "Ruelles Cryptées", "Un labyrinthe urbain rempli de caméras piratables.")
        self.rooms.append(ruelles)
        station_transit = Room( "Station de Transit", "Un nœud central reliant plusieurs quartiers de Neo-Delta.")
        self.rooms.append(station_transit)
        secteur_medical = Room( "Secteur Médical", "Un ancien centre médical. Des dossiers parlent d’expériences secrètes.")
        self.rooms.append(secteur_medical)
        quartier = Room( "Quartier Industriel", "Une zone dangereuse contrôlée par les forces d’ExoSys.")
        self.rooms.append(quartier)
        usine_recyclage = Room( "Usine de Recyclage", "Une usine abandonnée où des pièces cybernétiques sont encore récupérables.")
        self.rooms.append(usine_recyclage)
        centre_donnees = Room( "Centre de Données ExoSys", "Un bâtiment hautement sécurisé contenant des serveurs critiques.")
        self.rooms.append(centre_donnees)
        tours_corporatives = Room( "Tours Corporatives", "De hautes tours de verre abritant les dirigeants d’ExoSys.")
        self.rooms.append(tours_corporatives)
        ascenseur_neural = Room( "Ascenseur Neural", "Un ascenseur expérimental menant aux couches profondes du système.")
        self.rooms.append(ascenseur_neural)
        archives_numeriques = Room( "Archives Numériques", "Un espace étrange où données et réalité semblent se confondre.")
        self.rooms.append(archives_numeriques)
        reseau_fantome = Room( "Réseau Fantôme", "Un cyberspace instable rempli d’illusions et de données corrompues.")
        self.rooms.append(reseau_fantome)
        noyau_nexus = Room( "Noyau Nexus", "Le cœur de l’intelligence artificielle Nexus. Le choix final vous attend.")
        self.rooms.append(noyau_nexus)
        toits_neodelta = Room( "Toits de Neo-Delta", "Les toits de la ville offrent une vue globale sur Neo-Delta.")
        self.rooms.append(toits_neodelta)
        refuge_oublie = Room( "Refuge Oublié", "Un lieu secret contenant un message caché de Cipher." )
        self.rooms.append(refuge_oublie)


        # Création des sorties entre les pièces
        appart.exits = {"S":rue,"N":None,"E":None,"O":None}
        rue.exits = {"N":appart,"E":marche_noir,"S":ruelles,"O":station_transit}
        marche_noir.exits = {"E":rue,"S":serveur,"O":None,"N":None}
        serveur.exits = {"N":marche_noir,"O":None,"E":None,"S":None}
        ruelles.exits = {"N":rue,"O":quartier,"E":None,"S":None}
        station_transit.exits = {"E":rue,"S":quartier,"O":secteur_medical,"N":None}
        quartier.exits = {"N":station_transit,"E":ruelles,"O":None,"S":usine_recyclage}
        secteur_medical.exits = {"E":station_transit,"N":centre_donnees,"O":None,"S":None}
        centre_donnees.exits = {"S":secteur_medical,"O":tours_corporatives,"E":None,"N":None}
        tours_corporatives.exits = {"E":centre_donnees,"S":ascenseur_neural,"N":toits_neodelta,"O":refuge_oublie}
        ascenseur_neural.exits = {"N":tours_corporatives,"S":archives_numeriques,"E":None,"O":None}
        archives_numeriques.exits = {"N":ascenseur_neural,"S":reseau_fantome,"O":usine_recyclage,"E":None}
        reseau_fantome.exits = {"N":archives_numeriques,"S":noyau_nexus,"E":None,"O":None}
        noyau_nexus.exits = {"N":reseau_fantome,"E":None,"O":None,"S":None}
        toits_neodelta.exits = {"S":tours_corporatives,"E":None,"N":None,"O":None}
        refuge_oublie.exits = {"E":tours_corporatives,"N":None,"S":None,"O":None}
        usine_recyclage.exits = {"N":ruelles,"E":None,"O":None,"S":None}

        # Ajout d'objets dans les pièces
        appart.items.append(Item(name = "Chaise", description = "Une chaise en métal rouillée."))
        appart.items.append(Item("clé USB", "Une clé USB contenant des données cryptées."))
        # appart.items.append(Item("terminal", "Un terminal de hacking portable."))
        # marche_noir.items.append(Item("carte d'accès", "Une carte d'accès volée permettant d'entrer dans certaines zones."))
        # serveur.items.append(Item("disque dur", "Un vieux disque dur contenant des archives."))
        # secteur_medical.items.append(Item("dossier médical", "Un dossier parlant d'expériences secrètes."))
        # usine_recyclage.items.append(Item("pièce cybernétique", "Une pièce cybernétique récupérable."))
        # refuge_oublie.items.append(Item("message de Cipher", "Un message codé laissé par Cipher."))

        #Création du joueur
        self.player = Player(input("\nEntrez votre nom: "))
        self.player.current_room = appart

    def play(self):
        self.setup()
        self.print_welcome()
        while not self.finished:
            # Lire la commande de l'utilisateur
            self.process_cmd(input("\n>> "))
        return None

    def process_cmd(self, cmd_string) -> None:
        # Diviser la chaîne de commande en mots
        words = cmd_string.split()
        if not words:
            print("\nAucune commande entrée.\n")
            return
        cmd_word = words[0]
        if cmd_word not in self.cmd.keys():
            print(f"\nCommande '{cmd_word}' non reconnue. Entrez 'help' pour voir la liste des commandes disponibles.\n")
            return

        cmd = self.cmd[cmd_word]
        cmd.action(self, words, cmd.number_of_parameters)

    def print_welcome(self):
        print("\nBienvenue dans 'Nexus Infiltration' !")
        print(f"{self.player.name}, vous êtes un hacker dans la ville futuriste de Neo-Delta.")
        print("Votre mission est d'infiltrer le système central ExoSys et de découvrir ses secrets.")
        print("Entrez 'help' si vous avez besoin d'aide.\n")
        self.player.current_room.describe()
    
def main():
    Game().play()

if __name__ == "__main__":
    main()

