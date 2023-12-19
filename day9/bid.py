from art import logo
print(logo)


bidders={}
cont=False
def find_highest_bidder(bidding_records):
    highest_bid=0
    winer=''
    for bidder in bidding_records:
        bid_amount=bidding_records[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winer=bidder
    print(f"the winer is {winer} with highest number bids ${highest_bid} ")
while not cont:
   
    name=input("what is your name?:")
    price=int(input("enter bid number: $"))
    bidders[name]=price
    
    cont=input("do you want to continoue 'yes' or 'no': ")
    if cont == 'no':
        cont=True
        find_highest_bidder(bidders)
        
    elif cont == 'yes':
        cont=False