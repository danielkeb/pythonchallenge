import random
word_list=['abel','mulaturate','degener']
wor=random.choice(word_list)
display=[]

for _ in range(len(wor)):
    display+='_'
lenga=len(display)
print(lenga)
lives=6
while lenga>0 and '_' in display and lives>0:

    gu=input("guess letter ")
    if gu in display:
        print(f"you have already guessed: {gu}")
    lenga-=1
    for i in range(0,len(wor)):
        if gu==wor[i]:
            display[i]=gu
    if gu not in wor:
        lives-=1
        if lives==0:
            print("you lost")
    
   
    print(display)

if '_' not in display:
    print("you won")
else:
    print("you lost")
