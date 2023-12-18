from art import logo
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print(logo)
cont="yes"
while cont=="yes":
    text=input("enter text you want to 'encode' or 'decode': ").lower()
    if text=="encode" or text=="decode":

        def caesar(text):  
            cipher=input(f"enter you want to {text} message: ").lower()
            shift=int(input("enter shift: "))
            shift=shift % 25
            plaintext=''
            if text=='decode':
                shift*=-1
            for char in cipher:
                if char in alphabet:
                    n=alphabet.index(char)
                    new_position=n+shift
                    new_letter=alphabet[new_position]
                    plaintext+=new_letter  
                else:
                    plaintext+=char   

        
            print(f"{text}ed text is: {plaintext}")
        caesar(text)
    else:
        print("please enter encode or decode word")
    cont=input("if you want to continue 'yes' if not say no: ")
print("Goodbye!")    

