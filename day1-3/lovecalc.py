print("welcome to love calculator")
name1=input("enter your name: ")
name2=input("enter your crush name: ")
total= name1 + name2
lower=total.lower()
t=lower.count("t")
r=lower.count("r")
u=lower.count("u")
e=lower.count("e")

true=t+r+u+e

L=lower.count("l")
o=lower.count("o")
v=lower.count("v")
e=lower.count("e")

love=L+o+v+e
love_score=int(str(true)+str(love))
if love_score<10 or love_score>90:
  print(f"your score is {love_score}, you go together like coke and mentos")
elif love_score>40 and love_score<50:
  print(f"your score is {love_score}, you are alright together")
else:
  print(f"your love score is {love_score}")