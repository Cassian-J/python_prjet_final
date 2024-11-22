class Detection_Cycle:
    @staticmethod
    def detection(historic_table):
        if historic_table != []:
            for i in range(len(historic_table)-1):
                match_found = True
                if len(historic_table[len(historic_table)-1]) == len(historic_table[i]):
                    for j in range(len(historic_table[i])):
                        if historic_table[len(historic_table)-1][j] != historic_table[i][j]:
                            match_found = False
                    if match_found:
                        return i
        return -1
