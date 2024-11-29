import time

import generator_table
import update_table
import print_table
import historic
import detection_cycle
import save_game
import key_controle

class Game:
    """
        Classe principale qui gère le déroulement du jeu.
        Implemente l'initialisation, les interactions avec l'utilisateur,
        la sauvegarde et la détection de cycles, ainsi que la logique de mise à jour.
    """
    def __init__(self):
        """
            Initialisation du jeu :
            - Configure la taille de la table selon l'entrée utilisateur.
            - Initialise les modules nécessaires au fonctionnement.
        """
        key_controle.Key_Controle.clear()
        while True:
            try:
                self.col =int(input("Combien de colonnes et lignes voulez-vous dans cette partie ? (n x n)\n"))
                key_controle.Key_Controle.clear()
                if self.col < 3 or self.col >= 50:
                    print("Le nombre de colonnes et de lignes doivent être un entier positif, entre 3 et 49 compris.")
                else:
                    break
            except ValueError:
                key_controle.Key_Controle.clear()
                print("Veuillez entrer un nombre entier.")
        self.row=self.col
        self.table = generator_table.Generator_Table.generate(self.col, self.row, [0, 1])
        self.old_table_alive_cells = []
        self.historic = historic.Historic()
        self.detection = detection_cycle.Detection_Cycle()
        self.save_game = save_game.Save_Game()
        self.file="./save.txt"
        self.automatic=False

    def start_game(self):
        """
            Lance le jeu et gère le cycle de vie de la partie.
            - Permet de charger une partie existante ou d'en commencer une nouvelle.
            - Gère les modes manuel et automatique.
        """
        while True:
            try:
                print("[0] continuer la partie d'avant\n[1] commencer une nouvelle partie")
                new_game = int(key_controle.Key_Controle.get_key().lower())
                key_controle.Key_Controle.clear()
                if new_game != 0 and new_game != 1:
                    print("Le nombre choisi doit être 0 ou 1.")
                else:
                    break
            except ValueError:
                key_controle.Key_Controle.clear()
                print("Veuillez entrer 1 ou 0.")

        if new_game == 0:
            game = self.save_game.read_game_table(self.file)
            if game is None:
                self.end_game()
                breakpoint
            self.col, self.row = game[-1][-1][0], game[-1][-1][-1]
            self.table = generator_table.Generator_Table.generate_Table_game(
                generator_table.Generator_Table.generate(self.col, self.row, [0]), game[-1]
            )
        else:
            self.save_game.save_game_table(self.file, self.historic.old_table([], self.table))
            game = self.save_game.read_game_table(self.file)
            if game is None:
                self.end_game()
                breakpoint

        while True:
            key_controle.Key_Controle.clear()
            print("Ça fait", len(self.save_game.read_game_table(self.file)), "année que la population vit")
            print(print_table.Print_Table.print_game(self.table))

            debut_cycle = self.detection.detection(self.save_game.read_game_table(self.file))
            if debut_cycle != -1:
                print("Un cycle a été détecté. Il a commencé à la", debut_cycle, "année")
                if self.automatic:
                    self.automatic = False

            if not self.automatic:
                while True:
                    try:
                        print("[q] quittez\n[a] continuez automatiquement\n[c] continuez")
                        enter = key_controle.Key_Controle.get_key().lower()
                        if enter not in ['a', 'q', 'c']:
                            key_controle.Key_Controle.clear()
                            print("Ça fait", len(self.save_game.read_game_table(self.file)), "année que la population vit")
                            print(print_table.Print_Table.print_game(self.table))
                            print("Choix invalide!")
                        else:
                            break
                    except ValueError:
                        key_controle.Key_Controle.clear()
                        print("erreur du jeu")
            
                if enter == 'a':
                    self.automatic = True
                if enter == 'q':
                    self.end_game()
                    break
            else:
                print("Tapez sur [Entrée] pour arrété le mode automatique")
                time.sleep(0.25)
                if key_controle.Key_Controle.check_keypress():
                    key_controle.Key_Controle.clear()
                    self.automatic = False

            self.table = update_table.Update_Table.update(self.table)
            old_table = self.save_game.read_game_table(self.file)
            self.save_game.save_game_table(self.file, self.historic.old_table(old_table, self.table))

    
    def end_game(self):
        """
            Termine la partie en affichant un message.
        """
        key_controle.Key_Controle.clear()
        print("la partie est terminée")
        time.sleep(2.5)
        key_controle.Key_Controle.clear()
        return

