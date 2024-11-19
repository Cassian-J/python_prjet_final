class Historic:
    @staticmethod
    def ancien_table(table, new_table):
        alive_cells = Historic.list_alive_cells(new_table)
        table.append(alive_cells)
        return table

    @staticmethod
    def list_alive_cells(table):
        alive_cells = []
        for i in range(len(table)):
            for j in range(len(table[i])):
                if table[i][j] == 1:
                    alive_cells.append((i, j))
        return alive_cells

