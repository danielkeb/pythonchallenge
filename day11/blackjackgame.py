import random

def deal_card():
    """returns random card number"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0.
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare_score(user_score, computer_score):
    if computer_score == user_score:
        return "it's draw"
    elif computer_score ==0:
        return "Lose, opponent has blackjack"
    elif user_score == 0:
        return "win with blackjack"
    elif user_score>21:
        return "opponent went over. you lose"
    elif computer_score>21:
        return "opponent went over. you win"
    
    elif user_score > computer_score:
        return "you win"
    else:
        return "you lose"
      

    
def play_game():    
    user_card=[]
    computer_card=[]
    is_game_over=False
  
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())


    while not is_game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)
        print(f"user card: {user_card} ")
        print(f"user score: {user_score}, computer score: {computer_score}");
        


        if user_score ==0 or computer_score ==0 or user_score >21:
            is_game_over=True
        else:
            cont=input("if you want to continue game 'y' if not 'n' ")
            if cont =='y':
                user_card.append(deal_card())
            else:
                is_game_over=True



    while computer_score!=0 and computer_score<17:
        computer_card.append(deal_card())
        computer_score=calculate_score(computer_card)
    print(f"your current cards {user_card}, your score {user_score}")
    print(f"current computer cards {computer_card}, computer score {computer_score}")
    print(compare_score(user_score, computer_score))
while input("do you want to continoue 'y' or 'n'?")=='y':
    play_game()