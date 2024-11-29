import generator_table

class Update_Table:
    # Cette classe contient des méthodes pour mettre à jour une table
    @staticmethod
    def update(old_table):
        """
            Met à jour la table en appliquant les règles définies dans 
            `check_neighbors_condition` pour chaque cellule.
            
            :param old_table: La table actuelle (liste à 2 entrées) à mettre à jour.
            :return: Une nouvelle table (liste à 2 entrées) après application des règles.
        """
        new_table = generator_table.Generator_Table.generate(len(old_table[0]), len(old_table), [0])
        for row in range(len(old_table)):
            for col in range(len(old_table[row])):
                new_table[row][col] = Update_Table.check_neighbors_condition(old_table, row, col)
        return new_table

    @staticmethod
    def check_neighbors_condition(table, row, col):
        """
            Vérifie les conditions basées sur les voisins pour une cellule donnée.
            
            :param table: La table actuelle (liste à 2 entrées).
            :param row: L'indice de la ligne de la cellule à vérifier.
            :param col: L'indice de la colonne de la cellule à vérifier.
            :return: 1 si la cellule doit être vivante, 0 sinon.
        """
        positions = [(row-1, col), (row+1, col), (row, col-1), (row, col+1), (row-1, col-1), (row-1, col+1), (row+1, col-1), (row+1, col+1)]
        neighbors = 0
        for new_row, new_col in positions:
            if 0 <= new_row < len(table) and 0 <= new_col < len(table[0]):
                if table[new_row][new_col] == 1:
                    neighbors += 1
        if table[row][col] == 1:
            if neighbors >= 2 and neighbors <= 3:
                return 1
            else:
                return 0
        else:
            if neighbors == 3:
                return 1
            else:
                return 0
