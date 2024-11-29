import json

class Save_Game:
    """
        Classe pour sauvegarder et lire une table de jeu dans un fichier au format JSON.
        Fournit des méthodes pour écrire la table dans un fichier et pour la charger depuis un fichier.
    """
    def save_game_table(self,fileName, table):
        """
            Sauvegarde une table de jeu dans un fichier au format JSON.
            
            :param fileName: Le nom du fichier où la table doit être sauvegardée.
            :param table: La table de jeu (liste ou liste 2D) à sauvegarder.
        """
        try:
            with open(fileName, 'w') as file:
                json.dump(table, file)
        except Exception as error:
            print(f"Une erreur s'est produite : {error}")

    def read_game_table(self,fileName):
        """
            Lit une table de jeu à partir d'un fichier au format JSON.
            Si le fichier n'existe pas, crée un fichier vide par défaut et relance la lecture.
            
            :param fileName: Le nom du fichier à lire.
            :return: La table de jeu (liste ou liste 2D) si la lecture réussit, sinon `None`.
        """
        try:
            with open(fileName, 'r') as file:
                table = json.load(file)
                return table
        except FileNotFoundError:
                self.save_game_table(fileName,"[]")
                self.read_game_table(fileName)
        except Exception as error:
            print(f"Une erreur s'est produite : {error}")
            return None
    