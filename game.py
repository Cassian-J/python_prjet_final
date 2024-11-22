import generator_table
import update_table
import print_table
import historic
import detection_cycle
import save_game
import os
import time

class Game:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        while True:
            try:
                self.col = int(input("Combien de colonnes et lignes voulez-vous dans cette partie ? (n x n)\n"))
                os.system('cls' if os.name == 'nt' else 'clear')
                if self.col <= 0:
                    print("Le nombre de colonnes doit être un entier positif.")
                else:
                    break
            except ValueError:
                print("Veuillez entrer un nombre entier pour les colonnes.")
        self.row=self.col
        self.table = generator_table.Generator_Table.generate(self.col, self.row, [0, 1])
        self.old_table_alive_cells = []
        self.historic = historic.Historic()
        self.detection = detection_cycle.Detection_Cycle()
        self.save_game = save_game.Save_Game()
        self.file="./save.txt"

    def start_game(self):
        while True:
            try:
                new_game = int(input("[0] continuer la partie d'avant\n[1] commencer une nouvelle partie\n"))
                os.system('cls' if os.name == 'nt' else 'clear')
                if new_game != 0 and new_game!= 1:
                    print("Le nombre choisi doit etre 0 ou 1.")
                else:
                    break
            except ValueError:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Veuillez entrer 1 ou 0.")
        if new_game==0:
            game=self.save_game.read_game_table(self.file)
            if game==None:
                 self.end_game()
                 breakpoint
            self.col, self.row=game[-1][-1][0], game[-1][-1][-1]
            self.table=generator_table.Generator_Table.generate_Table_game(generator_table.Generator_Table.generate(self.col, self.row, [0]),game[-1])
        else:
            self.save_game.save_game_table(self.file,self.historic.old_table([],self.table))
            game=self.save_game.read_game_table(self.file)
            if game==None:
                 self.end_game()
                 breakpoint
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ça fait",len(self.save_game.read_game_table(self.file)),"année que la population vit")
            print(print_table.Print_Table.print(self.table))
            debut_cycle = self.detection.detection(self.save_game.read_game_table(self.file))
            if debut_cycle != -1:
                print("Un cycle a été détecté. Il a commencé à la",debut_cycle,"année")
            
            enter = input("Appuyez sur q pour quitter ou entrer pour continuer : ")
            if enter == 'q':
                self.end_game()
                break
            self.table = update_table.Update_Table.update(self.table)
            old_table=self.save_game.read_game_table(self.file)
            self.save_game.save_game_table(self.file,self.historic.old_table(old_table,self.table))
    
    def end_game(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("la partie est terminée")
        time.sleep(2.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        return

