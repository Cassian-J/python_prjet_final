
def print(table):
    printing="|---"*len(table[0])+"|\n"
    for column in range(len(table)):
        printing+="|"
        for line in range(len(table[i])):
            if table[column][line]==0:
                printing+="\033[40m   \033[0m|"
            elif table[column][line]==1:
                printing+="\033[47m   \033[0m|"
        printing+="\n"
        printing+=("|---"*len(table[column])+"|\n")
    return printing