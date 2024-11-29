
class Print_Table:
    """
        Classe utilitaire pour afficher une grille de jeu (table).
        Transforme une liste 2D en une chaîne de caractères lisible avec des symboles visuels.
    """
    @staticmethod
    def print_game(table):
        """
            Génère une représentation visuelle de la grille de jeu.

            :param table: Liste 2D représentant la grille de jeu.
                        Les valeurs de chaque cellule doivent être 0 ou 1.
            :return: Une chaîne de caractères représentant la grille, prête à être affichée.
        """
        printing = ""
        for row in range(len(table)):
            for col in range(len(table[row])):
                if table[row][col] == 0:
                    printing += "⬛"
                elif table[row][col] == 1:
                    printing += "⬜"
            printing += "\n"
        return printing
