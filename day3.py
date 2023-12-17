# print("welcome to the tip calculator")
# year=int(input("enter year you want to calculate: "))
# if year%4==0:
#   if year%100==0:
#     if year%400==0:
#       print("leap year")
#     else:
#      print("not leap year")
#   else:
#     print("leap year")
# else:
#   print("not leap year")
# print("welcome to pizza deliveries")
# bill=0
# size=input("what size pizza you want to order s, m, l: ")
# if size=="s":
#   bill=15
# elif size=="m":
#   bill=20
# elif size=="l":
#   bill=25
# else:
#   print("invalid input")
# add_pepperoni=input("do you want to add pepperoni y/n: ")
# if add_pepperoni=="y":
#   if size=="s":
#     bill=bill+2
#   elif size == "m" or size=="l":
#     bill=bill+3
  
# add_extra_cheese=input("do you want to add extra cheese y/n: ")
# if add_extra_cheese=="y":
#   bill=bill+1
# print(f"total your bill {bill}")
# print("welcome to love calculator")
# name1=input("enter your name: ")
# name2=input("enter your crush name: ")
# total= name1 + name2
# lower=total.lower()
# t=lower.count("t")
# r=lower.count("r")
# u=lower.count("u")
# e=lower.count("e")

# true=t+r+u+e

# L=lower.count("l")
# o=lower.count("o")
# v=lower.count("v")
# e=lower.count("e")

# love=L+o+v+e
# love_score=int(str(true)+str(love))
# if love_score<10 or love_score>90:
#   print(f"your score is {love_score}, you go together like coke and mentos")
# elif love_score>40 and love_score<50:
#   print(f"your score is {love_score}, you are alright together")
# else:
#   print(f"your score is {love_score}")
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
''')
print("welcome to treasure island your mission is to fins the treasure")
direction=input("you\" are at a cross roads, where do you want to go left or right: /")
if direction=="left":
  activity=input("you are at a lake, there is a boat, do you want to swim or wait: ")
  if activity=="swim":
    print("you drowned, game over")
  elif activity=="wait":
    doorcolor=input("which door red, blue or yellow: ")
    if doorcolor=="yellow":
      print("you found the treasure, congratulations")
    elif doorcolor=="blue":
      print("you fell in a hole, game over")
    elif doorcolor=="red":
      print("you walked into a tiger, game over")
    else:
      print("invalid input, game over")
else:
  print("you fell into a hole, game over")
