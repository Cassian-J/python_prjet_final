class Historic:
    """
        Classe utilitaire pour gérer l'historique des grilles de jeu.
        Permet de suivre les cellules vivantes à chaque étape et d'ajouter ces informations à l'historique.
    """
    @staticmethod
    def old_table(table, new_table):
        """
            Met à jour l'historique des grilles avec les cellules vivantes de la nouvelle grille.

            :param table: Liste représentant l'historique des cellules vivantes (chaque entrée est une liste de tuples).
            :param new_table: Nouvelle grille de jeu sous forme de liste 2D.
            :return: L'historique mis à jour avec les cellules vivantes de `new_table`.
        """
        alive_cells = Historic.list_alive_cells(new_table)
        table.append(alive_cells)
        return table

    @staticmethod
    def list_alive_cells(table):
        """
            Identifie les cellules vivantes dans une grille donnée.

            :param table: Grille de jeu sous forme de liste 2D.
            :return: Liste des coordonnées des cellules vivantes, suivie de la taille de la grille.
                    Exemple : [(row1, col1), (row2, col2), ..., (num_rows, num_cols)].
        """
        alive_cells = []
        for row in range(len(table)):
            for col in range(len(table[row])):
                if table[row][col] == 1:
                    alive_cells.append((row, col))
        alive_cells.append((len(table),len(table[row])))
        return alive_cells

