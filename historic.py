class Historic:
    @staticmethod
    def old_table(table, new_table):
        alive_cells = Historic.list_alive_cells(new_table)
        table.append(alive_cells)
        return table

    @staticmethod
    def list_alive_cells(table):
        alive_cells = []
        for row in range(len(table)):
            for col in range(len(table[row])):
                if table[row][col] == 1:
                    alive_cells.append((row, col))
        alive_cells.append((len(table),len(table[row])))
        return alive_cells

