import json

class Save_Game:
    def save_game_table(self,fileName, table):
        try:
            with open(fileName, 'w') as file:
                json.dump(table, file)
        except Exception as error:
            print(f"Une erreur s'est produite : {error}")

    def read_game_table(self,fileName):
        try:
            with open(fileName, 'r') as file:
                table = json.load(file)
                return table
        except FileNotFoundError:
                self.saveGameTable(fileName,"[]")
                self.readGameTable(fileName)
        except Exception as error:
            print(f"Une erreur s'est produite : {error}")
            return None
    