import generator_table

def update(ancien_table):
    new_table=generator_table.generate(len(ancien_table[0]),len(ancien_table),[0])
    for i in range(len(ancien_table)):
        for j in range(len(ancien_table[i])):
            new_table[i][j]=check_neighbors_condition(ancien_table,i,j)
    return new_table

def check_neighbors_condition(table, row, col):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    neighbors=0
    for rows,cols in directions:
        new_row, new_col=row+rows,col+cols
        if 0<=new_row<len(table) and 0<=new_col<len(table[0]):
            if table[new_row][new_col] == 1:
                neighbors += 1
    if table[row][col] == 1:
        if neighbors == 2 or neighbors==3:
            return 1
        else:
            return 0
    else:
        if neighbors == 3:
            return 1
        else:
            return 0