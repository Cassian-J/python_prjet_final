import generator_table

class Update_Table:
    @staticmethod
    def update(old_table):
        new_table = generator_table.Generator_Table.generate(len(old_table[0]), len(old_table), [0])
        for row in range(len(old_table)):
            for col in range(len(old_table[row])):
                new_table[row][col] = Update_Table.check_neighbors_condition(old_table, row, col)
        return new_table

    @staticmethod
    def check_neighbors_condition(table, row, col):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        neighbors = 0
        for rows, cols in directions:
            new_row, new_col = row + rows, col + cols
            if 0 <= new_row < len(table) and 0 <= new_col < len(table[0]):
                if table[new_row][new_col] == 1:
                    neighbors += 1
        if table[row][col] == 1:
            if neighbors == 2 or neighbors == 3:
                return 1
            else:
                return 0
        else:
            if neighbors == 3:
                return 1
            else:
                return 0
