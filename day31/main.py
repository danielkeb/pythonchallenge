from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
import pandas as pd
import random
try:
    data=pd.read_csv("./data/known_words.csv")
except:
    dat=pd.read_csv("./data/french_words.csv") 
    
    tolearn=dat.to_dict(orient='records')

else:

    tolearn=data.to_dict(orient='records')

finally:
#print(tolearn)
    lag={}
    def next_word():
        canvas.itemconfig(card_backgrund, image=card_front)
        global lag
        global flip_timer
        lag=random.choice(tolearn)
        canvas.itemconfig(title, text='French', fill='black')
        canvas.itemconfig(word, tex=f"{lag['French']}", fill='black')
        flip_timer = window.after(3000,flip_card)
    # with open("onkown_words.csv",'w') as fl:
    #     fl.write(f"{}"



    def flip_card():
        canvas.itemconfig(title, text='English', fill='white')
        canvas.itemconfig(word, tex=f"{lag['English']}",fill='white')
        canvas.itemconfig(card_backgrund, image=cardimage)

    def known():
        tolearn.remove(lag)
        # print(len(tolearn))
        data=pd.DataFrame(tolearn)
        data.to_csv("./data/known_words.csv", index=False)
        next_word()

window=Tk()

window.title("flashy")
flip_timer= window.after(3000,flip_card)
window.config(padx=20,pady=20, bg=BACKGROUND_COLOR)

canvas=Canvas(width=800, height=526)

cardimage=PhotoImage(file="./images/card_back.png")
card_front=PhotoImage(file="./images/card_front.png")
card_backgrund=canvas.create_image(400, 263, image=card_front)
canvas.grid(column=0, row=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

title=canvas.create_text(400, 150, text="Title", font=('Arial',40,'italic'))
word=canvas.create_text(400, 263, text="word", font=('Arial',40,'bold'))


wrong=PhotoImage(file="./images/wrong.png")
butto1=Button(image=wrong, highlightthickness=0,command=next_word)
butto1.grid(column=0, row=1)



right=PhotoImage(file="./images/right.png")
butto2=Button(image=right, highlightthickness=0,command=known)
butto2.grid(column=1, row=1)


next_word()

window.mainloop()