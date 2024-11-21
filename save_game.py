import json

class SaveGame:
    def saveGameTable(self,fileName, table):
        try:
            with open(fileName, 'w') as file:
                json.dump(table, file)
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")

    def readGameTable(self,fileName):
        try:
            with open(fileName, 'r') as file:
                table = json.load(file)
                return table
        except FileNotFoundError:
                self.saveGameTable(fileName,"[]")
                self.readGameTable(fileName)
        except Exception as e:
            print(f"Une erreur s'est produite : {e}")
            return None
    