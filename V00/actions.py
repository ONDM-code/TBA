#Description du fichier : VOO/actions.py
#Ce fichier contient les actions ue joueur peut effectuer dans le jeu textuel .

# Messages d'erreur
M0 = "La commande {cmd} n'est pas reconnue. Veuillez réessayer." # Message pour une commande invalide
M1 = "La commande {cmd} prend un seul argument." # Message pour un nombre incorrect d'arguments ou paramètres
M2 = "Argument manquant à {cmd}." # Message pour un argument manquant
M3 = "Argument invalide." # Message pour un argument invalide
M4 = "Accès refusé : autorisation insuffisante." # Message pour un accès refusé
M5 = "Connexion au serveur impossible." # Message pour une connexion échouée
M6 = "Données corrompues détectées." # Message pour des données corrompues
M7 = "Action impossible dans l'état actuel du système." # Message pour une action impossible
M8 = "Ressource introuvable." # Message pour une ressource non trouvée
M9 = "Commande bloquée par le protocole de sécurité Nexus." # Message pour une commande bloquée par la sécurité

# Actions du joueur

class Actions :
    
    @staticmethod
    def go(game , words , parameters) :
        """
        Déplacer le joueur dans la direction spécifiée.
        Paramètres : Points cardinaux (N , S , E , O).

        Args :
            game (Game) : Instance du jeu.
            words (list) : Liste des mots de la commande.
            parameters (list) : Le nombre de paramètres attendues par la commande.

        Returns :
            bool : True si le déplacement est réussi, False sinon.

        Exemples:
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> go(game ,   ['go' , 'N'] , 1)
        True
        >>> go(game ,   ['go' , 'up'] , 1)
        False
        >>> go (game ,   ['go'] , "N" , "E" , 1)
        False

        """
        player = game.player
        l = len(words)

        # Vérifier le nombre de paramètres , sinon conforme afficher un message d'erreur
        if l != parameters + 1:
            cmd = words[0]
            print(M1.format(cmd = cmd))
            return False
        
        # Prendre la direction de déplacement (normalisée en majuscules)
        direction = words[1].upper()
        # Déplacer le joueur dans la direction spécifiée et retourner le résultat
        return player.move(direction)
    
    @staticmethod
    def look (game,words,parameters):
        """
        Permet au joueur d'examiner son environnement immédiat.
        Paramètres : Points cardinaux (N , S , E , O)

        Args :
            game (Game) : Instance du jeu.
            words (list) : Liste des mots de la commande.
            parameters (list) : Le nombre de paramètres attendues par la commande.

        Returns :
            bool : True si l'examen est réussi, False sinon.

        Exemples:
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> look(game ,   ['look'] , 0)
        False
        >>> look(game ,   ['look' , 'around'] , 0)
        False
        >>> look (game ,   ['look' , 'N'] , 0)
        True

        """
        player = game.player
        l = len(words)

        # Autoriser "look" seul ou avec une direction
        if l not in (1, parameters + 1):
            cmd = words[0]
            print(M2.format(cmd = cmd))
            return False

        current_room = player.current_room

        # Sans direction : décrire la pièce actuelle
        if l == 1:
            current_room.describe()
            return True

        # Avec direction : décrire la pièce visée si elle existe
        direction = words[1].upper()
        next_room = current_room.get_exit(direction)
        if next_room is None:
            print("Aucune sortie dans cette direction.")
            return False

        print(next_room.description)
        return True
    
    @staticmethod
    def help (game,words,parameters):
        """
        Afficher la liste des commandes disponibles.

        Args :
            game (Game) : Instance du jeu.
            words (list) : Liste des mots de la commande.
            parameters (list) : Le nombre de paramètres attendues par la commande.

        Returns :
            bool : True si l'aide est affichée, False sinon.

        Exemples:
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> help(game ,   ['help'] , 0)
        True
        >>> help(game ,   ['help' , 'me'] , 0)
        False
        >>> help (game ,   ['assist'] , 0)
        False
        >>> help (game ,"go" , 0)
        True

        """
        l = len(words)

        # Vérifier le nombre de paramètres , sinon  afficher un message d'erreur
        if l != parameters + 1:
            cmd = words[0]
            print(M0.format(cmd = cmd))
            return False
        
        if words[0] != "help":
            cmd = words[0]
            print(M0.format(cmd = cmd))
            return False
        
        # Afficher le message d'aide approprié
        if l == 1:
            help_message = """ 
        Commandes disponibles :
        - go <direction> : Déplacer le joueur dans la direction spécifiée (N, S, E, O).
        - look [direction] : Examiner l'environnement actuel ou dans une direction.
        - take <objet> : Prendre un objet dans la pièce.
        - inventory : Afficher votre inventaire.
        - quit : Quitter le jeu.
        - help : Afficher ce message d'aide.
        """
            print(help_message)
        elif l == 2:
            if words[1] == "go":
                help_go = """
        Commande 'go' :
        - Déplacer le joueur dans la direction spécifiée.
        - Paramètres : N (Nord), S (Sud), E (Est), O (Ouest).
        - Exemple : go N
        """
                print(help_go)
            elif words[1] == "look":
                help_look = """
        Commande 'look' :
        - Examiner l'environnement immédiat dans la direction spécifiée.
        - Paramètres : N (Nord), S (Sud), E (Est), O (Ouest).
        - Exemple : look N
        """
                print(help_look)
            else:
                print(M3)
                return False
        
        return True
    
    @staticmethod
    def quit (game,words,parameters):
        """
        quitter le jeu.

        Args : 
            game (Game) : Instance du jeu.
            words (list) : Liste des mots de la commande.
            parameters (list) : Le nombre de paramètres attendues par la commande.
        
        Returns :
            bool : True si le jeu est quitté, False sinon.

        Exemples:
        >>> from game import Game
        >>> game = Game()
        >>> game.setup()
        >>> quit(game , "quit" , 0)
        True
        >>> quit(game ,   "quit" , "now" , 0)
        False
        >>> quit (game , "N" , 0)
        False

        """
        l = len(words)

        # Vérifier le nombre de paramètres , sinon  afficher un message d'erreur
        if l != parameters + 1:
            cmd = words[0]
            print(M0.format(cmd = cmd))
            return False
        
        # Placer l'attribut de fin du jeu à True
        player = game.player
        msg = f"\nMerci à toi , {player.name} d'avoir joué. À bientôt !\n"
        print(msg)
        game.finished = True
        return True
    
    @staticmethod
    def take(game, words, parameters):
        """
        Prendre un objet dans la pièce actuelle.

        Args :
            game (Game) : Instance du jeu.
            words (list) : Liste des mots de la commande.
            parameters (int) : Le nombre de paramètres attendues par la commande.

        Returns :
            bool : True si l'objet est pris, False sinon.
        """
        player = game.player
        l = len(words)

        # Vérifier le nombre de paramètres
        if l != parameters + 1:
            cmd = words[0]
            print(M1.format(cmd=cmd))
            return False

        # Récupérer le nom de l'objet (rejoindre les mots restants)
        item_name = " ".join(words[1:]).lower()
        current_room = player.current_room

        # Chercher l'objet dans la pièce
        for item in current_room.items:
            if item.name.lower() == item_name:
                current_room.items.remove(item)
                player.inventory.append(item)
                print(f"\nVous avez pris : {item.name}\n")
                return True

        print(f"\nL'objet '{item_name}' n'est pas ici.\n")
        return False

    @staticmethod
    def inventory(game, words, parameters):
        """
        Afficher l'inventaire du joueur.

        Args :
            game (Game) : Instance du jeu.
            words (list) : Liste des mots de la commande.
            parameters (int) : Le nombre de paramètres attendues par la commande.

        Returns :
            bool : True si l'inventaire est affiché, False sinon.
        """
        player = game.player
        l = len(words)

        # Vérifier le nombre de paramètres
        if l != parameters + 1:
            cmd = words[0]
            print(M0.format(cmd=cmd))
            return False

        # Afficher l'inventaire
        if not player.inventory:
            print("\nVotre inventaire est vide.\n")
        else:
            print("\nInventaire :")
            for item in player.inventory:
                print(f"  - {item.name}: {item.description}")
            print()

        return True




    



