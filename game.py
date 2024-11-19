import generator_table
import update_table
import print_table
import historic
import detection_cycle

col= int(input("how many column do you want to have for the game? "))
row= int(input("how many line do you want to have for the game? "))
table=generator_table.generate(col,row,[0,1])
ancien_table_alive_cells =[]
while True:
    print(print_table.print(table))
    debut_cycle=detection_cycle.detection(historic.list_alive_cells(table),ancien_table_alive_cells)
    if debut_cycle!=-1:
        print("un cycle a été detecté. il a commencer a l'itération :",debut_cycle)
        break
    enter = input("press q to quit or enter to continue :")
    if enter=='q':
        break
    ancien_table_alive_cells =historic.ancien_table(ancien_table_alive_cells,table)
    table = update_table.update(table)