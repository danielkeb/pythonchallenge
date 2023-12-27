from art import logo
print(logo)


cont=True
while cont:
    name=input("what is your name?:")
    bid=int(input("enter bid number"))
    
    cont=input("do you want to continoue 'yes' or 'no': ")
    if cont == 'yes':
        cont=True
    elif cont == 'no':
        cont=False
print(f"your bid number is  ${bid}")
    