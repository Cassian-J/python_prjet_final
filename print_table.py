
class PrintTable:
    @staticmethod
    def print(table):
        printing = ""
        for row in range(len(table)):
            for col in range(len(table[row])):
                if table[row][col] == 0:
                    printing += "⬛"
                elif table[row][col] == 1:
                    printing += "⬜"
            printing += "\n"
        return printing
