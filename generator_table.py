import random

class GeneratorTable:
    @staticmethod
    def generate(col, row, table):
        return [[random.choice(table) for _ in range(col)] for _ in range(row)]
    
    def generate_Table_game(table, positions):
        for x, y in positions:
            if 0 <= x < len(table) and 0 <= y < len(table[0]): 
                table[x][y] = 1
        return table