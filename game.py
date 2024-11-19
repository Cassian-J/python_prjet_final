import generator_table
import update_table
import print_table

x= int(input("how many column do you want to have for the game? "))
y= int(input("how many line do you want to have for the game? "))
table=generator_table.generate(x,y,[0,1])
print(print_table.print(table))