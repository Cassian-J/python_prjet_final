import generator_table
import update_table
import print_table

col= int(input("how many column do you want to have for the game? "))
row= int(input("how many line do you want to have for the game? "))
table=generator_table.generate(col,row,[0,1])
while True:
    print(print_table.print(table))
    enter = input("press q to quit or enter to continue :")
    if enter=='q':
        break
    table = update_table.update(table)