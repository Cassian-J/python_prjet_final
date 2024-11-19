def detection(table,historic_table):
    if historic_table!=[]:
        for i in range(len(historic_table)):
            match_found = True
            if len(table)==len(historic_table[i]):
                for j in range(len(historic_table[i])):
                    if table[j]!=historic_table[i][j]:
                        match_found = False
                if match_found:
                    return i
    return -1