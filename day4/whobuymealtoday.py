import random
names_strin=input("give a name that separated by commas ")
names= names_strin.split(",")
n=len(names)

pay=random.randint(0,n-1)

print(names[pay] +" going to buy meal today")

