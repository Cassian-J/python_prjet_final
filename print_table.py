
class PrintTable:
    @staticmethod
    def print(table):
        printing = "|---" * len(table[0]) + "|\n"
        for col in range(len(table)):
            printing += "|"
            for row in range(len(table[col])):
                if table[col][row] == 0:
                    printing += "\033[40m   \033[0m|"
                elif table[col][row] == 1:
                    printing += "\033[47m   \033[0m|"
            printing += "\n"
            printing += ("|---" * len(table[col]) + "|\n")
        return printing
