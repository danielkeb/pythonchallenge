from prettytable import PrettyTable

table=PrettyTable()

table.add_column('Pokemon Name',['pikachu', 'SQuirtle', 'Charmander'])
table.add_column('Type',['Electric', 'water', 'Fire'])
table.align="l"
print(table)