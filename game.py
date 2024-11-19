import generator_table
import update_table
import print_table
import historic
import detection_cycle

class Game:
    def __init__(self):
        self.col = int(input("How many columns do you want to have for the game? "))
        self.row = int(input("How many rows do you want to have for the game? "))
        self.table = generator_table.GeneratorTable.generate(self.col, self.row, [0, 1])
        self.ancien_table_alive_cells = []
        self.historic = historic.Historic()
        self.detection = detection_cycle.DetectionCycle()

    def start_game(self):
        self.ancien_table_alive_cells = self.historic.ancien_table(self.ancien_table_alive_cells, self.table)
        
        while True:
            print(print_table.PrintTable.print(self.table))
            debut_cycle = self.detection.detection(self.historic.list_alive_cells(self.table), self.ancien_table_alive_cells)
            
            if debut_cycle != -1:
                print("A cycle has been detected. It started at iteration:", debut_cycle)
                break
            
            enter = input("Press q to quit or enter to continue: ")
            if enter == 'q':
                break
            #print("vous êtes a l'itération :",len(self.historic.ancien_table))
            self.table = update_table.UpdateTable.update(self.table)
            self.ancien_table_alive_cells = self.historic.ancien_table(self.ancien_table_alive_cells, self.table)

def run_game():
    game = Game()
    game.start_game()

if __name__ == "__main__":
    run_game() 