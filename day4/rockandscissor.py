import random
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
    