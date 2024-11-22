
class PrintTable:
    @staticmethod
    def print(table):
        printing = ""
        for col in range(len(table)):
            for row in range(len(table[col])):
                if table[col][row] == 0:
                    printing += "⬛"
                elif table[col][row] == 1:
                    printing += "⬜"
            printing += "\n"
        return printing
