import random
from data import data
is_game_over=False
count_score=0
while not is_game_over:

    
    ind1=random.randint(0,3)
    ind2 = random.randint(0,3)
    if ind1!=ind2:

        print(f"{data[ind1]['name'] },{data[ind1]['description']} ,from {data[ind1]['country']}. ")
        print(" VS") 
        print(f"{data[ind2]['name']}, {data[ind2]['description']} ,from {data[ind2]['country']}. ")
        chos=input(f"who is high flower  'A' OR 'B' ").upper()
        if data[ind1]['follower_count']>data[ind2]['follower_count'] and chos=='A':
            
            count_score+=1
            print(f"you correct ,your current score is: {count_score}")
            is_game_over=False
        elif data[ind1]['follower_count']< data[ind2]['follower_count'] and chos=='B':
            count_score+=1
            is_game_over=False
            print(f"you correct ,your current score is: {count_score}")
        else:
            print(f"sorry wrong's ,your final score is: {count_score}")
            is_game_over=True
    else:
        ind1=random.randint(0,3)
        ind2=random.randint(0,3)
    



