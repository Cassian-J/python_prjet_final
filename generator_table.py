import random

class Generator_Table:
    """
        Classe utilitaire pour générer et modifier des grilles de jeu (tables).
        Permet de créer une grille aléatoire ou de définir des positions spécifiques.
    """
    @staticmethod
    def generate(col, row, table):
        """
            Génère une grille de jeu aléatoire avec les dimensions spécifiées.

            :param col: Nombre de colonnes dans la grille.
            :param row: Nombre de lignes dans la grille.
            :param table: Liste des valeurs possibles pour chaque cellule (ex : [0, 1]).
            :return: Grille de jeu aléatoire sous forme de liste 2D.
        """
        return [[random.choice(table) for _ in range(col)] for _ in range(row)]
    
    def generate_Table_game(table, positions):
        """
            Modifie une grille de jeu en activant certaines positions spécifiées.

            :param table: La grille de jeu sous forme de liste 2D.
            :param positions: Liste de tuples représentant les coordonnées (ligne, colonne) à activer.
            :return: La grille de jeu modifiée.
        """
        for row, col in positions:
            if 0 <= row < len(table) and 0 <= col < len(table[0]): 
                table[row][col] = 1
        return table