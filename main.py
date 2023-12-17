import random
# import random_1
# # rannd_nnum=random.randint(1,100)
# # print (rannd_nnum)
# print(random_1.pi)
# float_rand = random.uniform(1,5)
# print(float_rand)

# da="daniel"
# n = da.count("d")
# print(n)
# num=random.randint(0,1)
# if num == 0:
#     print("Heads")
# else:
#     print("tails")
# names_strin=input("give a name that separated by commas ")
# names= names_strin.split(",")
# n=len(names)

# pay=random.randint(0,n-1)

# print(names[pay] +" going to buy meal today")
# fruits=["cash", "food","ejected", "gross"]
# vagetables=["money", "junk","ehlo", "groop"]
# dirty = [['cash', 'food', 'ejected', 'gross'], ['money', 'junk', 'ehlo', 'groop']]
# print(dirty[1][0])
# row1=["cash", 'food', "knowledge"]
# row2=["cas", 'foo', 'know']
# row3=["ash", 'od', 'ledge']
# map=[row2, row2, row3]
# print(f"{row1}\n {row2}\n {row3}\n")
# n=input("when you wnat to put the treasure")
# column=int(n[0])
# row=int(n[1])
# map[column][row]="x"
# print(f"{row1}\n {row2}\n {row3}\n")
game=[
    "rock image",
    "scissor image",
    "paper image"
    ]


rock=input("choose for rock 1 ,scissors 2 paper 3: ")
me= int(rock)
if me > 3 or me < 0:
    print("Please valid number")
else:
    print(f"me choosed {me}")
    computer = random.randint(1,3)
    print(f"{game[computer-1]} choosed :{computer}")
    if (me==1  and computer==3) or me ==2 and computer==1:
        print("computer win")
    elif me==1 and computer==2 or (me==3 and computer==1):
        print("you win")    
    elif me==3 and computer==2: 
        print("you lose")
    elif computer==me:
        print("twin with computer")
    elif me==2 and computer==3:
        print("you win")
    


