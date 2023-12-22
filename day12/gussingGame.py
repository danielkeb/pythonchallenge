#from art import logo
import random
#print(logo)
def game(attempt):
    num1=random.randint(0,100)
    is_game_over=False
    while not is_game_over:
        me=int(input("Make guess: "))
        if num1>me:
            print("Too low")
            print("Guess again")
        elif me>num1:
            print("Too high")
            print("Guess again")
        elif me==num1:
            print("you got it")
            is_game_over=True
        attempt-=1
        if attempt==0:
            print("you have run out of the guess, you lose")
            is_game_over=True
        if attempt>0 and me!=num1:
           print(f"you have {attempt} attempts to guess the number")
    



# def hard_game():
#     num1=random.randint(0,100)
#     print(num1)
#     attempt=5
#     is_game_over=False
#     while not is_game_over:
#         me=int(input("Make guess: "))
#         if num1>me:
#             print("Too low")
#             print("Guess again")
#         elif me>num1:
#             print("Too high")
#             print("Guess again")
#         elif me==num1:
#             print("you got it")
#             is_game_over=True
#         attempt-=1
#         if attempt==0:
#             print("you lose")
#             is_game_over=True
#         print(f"you have {attempt} attempts to guess the number")


print("Welcome to the number Guessing Game!")
print("I'm thinnking of a nnumber between 1 and 100")
chose=input("choose difficulty. Type 'easy' or 'hard': ")
if chose=='easy':
    print("you have 10 attempts remaining to guess the number")
    game(10)
else:
    print("you have 5 attempts remaining to guess the number")
    game(5)
