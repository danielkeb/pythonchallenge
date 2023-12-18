import random
fruits=["cash", "food","ejected", "gross"]
vagetables=["money", "junk","ehlo", "groop"]
dirty = [['cash', 'food', 'ejected', 'gross'], ['money', 'junk', 'ehlo', 'groop']]
row1=["cash", 'food', "knowledge"]
row2=["cas", 'foo', 'know']
row3=["ash", 'od', 'ledge']
map=[row2, row2, row3]
numb=["1",     "2",      "3",]
print(numb)
print(f"1{row1}\n 2{row2}\n 3{row3}\n")
n=input("when you want to put the treasure")
column=int(n[0])
row=int(n[1])
map[column][row]="x"
print(f"{row1}\n {row2}\n {row3}\n")
