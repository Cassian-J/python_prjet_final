import generator_table
import update_table
import print_table
import historic
import detection_cycle
import save_game
import os

class Game:
    def __init__(self):
        self.col = int(input("How many columns do you want to have for the game? "))
        self.row = int(input("How many rows do you want to have for the game? "))
        self.table = generator_table.GeneratorTable.generate(self.col, self.row, [0, 1])
        self.ancien_table_alive_cells = []
        self.historic = historic.Historic()
        self.detection = detection_cycle.DetectionCycle()
        self.saveGame = save_game.SaveGame()
        self.file="./game.txt"

    def start_game(self):
        new_game = int(input("[0] continuer la partie\n[1] commencer une nouvelle partie\n"))
        if new_game==0:
            game=self.saveGame.readGameTable(self.file)
            if game==None:
                 self.end_game()
                 breakpoint
            print(game[-1])
            self.table=generator_table.GeneratorTable.generate_Table_game(generator_table.GeneratorTable.generate(self.col, self.row, [0]),game[-1])
        if new_game==1:
            self.saveGame.saveGameTable(self.file,self.historic.ancien_table([],self.table))
            game=self.saveGame.readGameTable(self.file)
            if game==None:
                 self.end_game()
                 breakpoint
            print(game[-1])
        while True:
            #os.system('cls' if os.name == 'nt' else 'clear')
            print("Ca fait",len(self.saveGame.readGameTable(self.file)),"année que la population vit")
            print(print_table.PrintTable.print(self.table))
            debut_cycle = self.detection.detection(self.saveGame.readGameTable(self.file))
            if debut_cycle != -1:
                print("A cycle has been detected. It started at iteration:", debut_cycle)
                self.end_game()
                break
            
            enter = input("Press q to quit or enter to continue: ")
            if enter == 'q':
                self.end_game()
                break
            self.table = update_table.UpdateTable.update(self.table)
            ancien_table=self.saveGame.readGameTable(self.file)
            self.saveGame.saveGameTable(self.file,self.historic.ancien_table(ancien_table,self.table))
    
    def end_game(self):
        print("le partie est terminer")


def run_game():
    game = Game()
    game.start_game()

if __name__ == "__main__":
    run_game() 