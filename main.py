import game
def run_game():
    """
        Fonction principale pour exécuter le jeu.
        Instancie la classe `Game` et démarre le jeu via sa méthode `start_game`.
    """
    gameClass = game.Game()
    gameClass.start_game()

if __name__ == "__main__":
    """
        Point d'entrée du programme.
        Vérifie si le fichier est exécuté directement (et non importé comme module),
        puis appelle la fonction `run_game`.
    """
    run_game() 