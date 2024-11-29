class Detection_Cycle:
    """
        Classe utilitaire pour détecter les cycles dans l'évolution des grilles de jeu.
        Un cycle se produit lorsque la configuration actuelle de la grille correspond exactement à une configuration précédente.
    """
    @staticmethod
    def detection(historic_table):
        """
            Détecte si la grille actuelle est identique à une configuration précédente (cycle).

            :param historic_table: Liste contenant l'historique des configurations de la grille.
                                Chaque élément représente une étape (année) de l'évolution de la grille.
            :return: L'indice (année) de la première occurrence de la configuration actuelle dans l'historique.
                    Retourne -1 si aucun cycle n'est détecté.
        """
        if historic_table != []:
            for years in range(len(historic_table)-1):
                if len(historic_table[len(historic_table)-1]) == len(historic_table[years]):
                    if historic_table[len(historic_table)-1] == historic_table[years]:
                        return years
        return -1
