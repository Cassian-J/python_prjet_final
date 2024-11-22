class Detection_Cycle:
    @staticmethod
    def detection(historic_table):
        if historic_table != []:
            for years in range(len(historic_table)-1):
                if len(historic_table[len(historic_table)-1]) == len(historic_table[years]):
                    if historic_table[len(historic_table)-1] == historic_table[years]:
                        return years
        return -1
