import generator_table
import update_table
import print_table
import historic
import detection_cycle
import save_game
import os

class Game:
    def __init__(self):
        self.col = int(input("combien de colonne voulez-vous dans cette partie ? "))
        self.row = int(input("combien de ligne voulez-vous dans cette partie ? "))
        self.table = generator_table.GeneratorTable.generate(self.col, self.row, [0, 1])
        self.ancien_table_alive_cells = []
        self.historic = historic.Historic()
        self.detection = detection_cycle.DetectionCycle()
        self.saveGame = save_game.SaveGame()
        self.file="./game.txt"

    def start_game(self):
        new_game = int(input("[0] continuer la partie d'avant\n[1] commencer une nouvelle partie\n"))
        if new_game==0:
            game=self.saveGame.readGameTable(self.file)
            if game==None:
                 self.end_game()
                 breakpoint
            self.col, self.row=game[-1][-1][0], game[-1][-1][-1]
            self.table=generator_table.GeneratorTable.generate_Table_game(generator_table.GeneratorTable.generate(self.col, self.row, [0]),game[-1])
        if new_game==1:
            self.saveGame.saveGameTable(self.file,self.historic.ancien_table([],self.table))
            game=self.saveGame.readGameTable(self.file)
            if game==None:
                 self.end_game()
                 breakpoint
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Ça fait",len(self.saveGame.readGameTable(self.file)),"année que la population vit")
            print(print_table.PrintTable.print(self.table))
            debut_cycle = self.detection.detection(self.saveGame.readGameTable(self.file))
            if debut_cycle != -1:
                print("Un cycle a été détecté. Il a commencé à la",debut_cycle+"e année")
                self.end_game()
                break
            
            enter = input("Appuyez sur q pour quitter ou entrer pour continuer : ")
            if enter == 'q':
                self.end_game()
                break
            self.table = update_table.UpdateTable.update(self.table)
            ancien_table=self.saveGame.readGameTable(self.file)
            self.saveGame.saveGameTable(self.file,self.historic.ancien_table(ancien_table,self.table))
    
    def end_game(self):
        print("la partie est terminée")
