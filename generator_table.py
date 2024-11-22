import random

class Generator_Table:
    @staticmethod
    def generate(col, row, table):
        return [[random.choice(table) for _ in range(col)] for _ in range(row)]
    
    def generate_Table_game(table, positions):
        for row, col in positions:
            if 0 <= row < len(table) and 0 <= col < len(table[0]): 
                table[row][col] = 1
        return table