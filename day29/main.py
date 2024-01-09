import json
from tkinter import *
from tkinter import messagebox
import pyperclip
import random
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)
def password_generator():
    alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K','L', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'b', 'd', 'e','f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','b','d','e','f']
    numbers=['0','1','2','3','4','5','6','7','8','9']
    especialsymbol=['~','%','&','*','!','(','-',')','+','$']
    map=[alphabets,numbers,especialsymbol]
    # print("welcome to password generator")
    # passlength=int(input("Enter your password length: "))
    # symblo=int(input("how many input you want to use: "))
    # num=int(input("how many numbers you want to use: "))
    passlength=random.randint(8,10)
    symbol=random.randint(2,4)
    num=random.randint(2,4)
    password=[
    random.choice(alphabets) for char in range(passlength)] + [random.choice(especialsymbol) for j in range(symbol)  ]+[random.choice(numbers) for k in range(num)]

    #print(f"your generated password is: {letter}") 
    random.shuffle(password)

    passwd="".join(password)
    # for char in password:
    #     passwd+= char
    password_entry.insert(0, passwd)
    pyperclip.copy(passwd)
   # print(passwd)

    #with open("data.txt", "r") as f:
        #print(f.readlines())

def save():

    website_label = web_entry.get()
    email_label=email_entry.get()
    password_label = password_entry.get()
    data_store= {
        website_label:{
        
            'email':email_label,
    
            'password':password_label
        }

    }
    if website_label=="" or email_label=="" or password_label=="":
        messagebox.showinfo(title="Oops!", message="please make sure you haven't left any fields empty")
    else:
        try:
            with open('data.json','r') as file:
                data=json.load(file)
                
                #json.dump(data_store, file, indent=4),
        except FileNotFoundError:
            with open('data.json','w') as file:
                json.dump(data_store, file, indent=4)
          
        else:
            data.update(data_store)
            with open('data.json','w') as file:
                json.dump(data, file, indent=4)

        finally:
            web_entry.delete(0, END)  
            password_entry.delete(0, END)

def search():
    try:
        website_label=web_entry.get()
        with open("data.json", "r") as dt:
            file=json.load(dt)
           

    except FileNotFoundError:
        messagebox.showinfo(title="error", message="File not found")
    else:
        if website_label in file:
            email=file[website_label]['email']
            password=file[website_label]['password']
            messagebox.showinfo(title=website_label, message=f"email :{email}\n password :{password}")
        else:
            messagebox.showinfo(title=website_label, message="website name ot found")
    
            
    finally:
        print("successfully")

canvas = Canvas(width=200, height=200, highlightthickness=0)
photo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1, row=0, pady=20)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

web_entry = Entry(width=20)
web_entry.grid(column=1, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0,'danielkebede381@gmail.com')

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, pady=0)  # Adjusted pady value

gen_password_button = Button(text="Generate Password", command=password_generator )
gen_password_button.grid(column=2, row=3, pady=0)  # Adjusted pady value

add_button = Button(text="Add", width=35, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=20)
search_button = Button(text="Search", width=15, command=search)
search_button.grid(column=2, row=1)




window.mainloop()
