from tkinter import *

window = Tk()

window.title("my first tkinter ")
window.minsize(width= 500, height= 300)
window.config(padx=20, pady=20)

my_label=Label(text='My first tkinter', font=("Arial",20,'italic'))





def button_clicked():
    txt=input.get()
    my_label.config(text=txt)

button= Button(text="clicked me ", command=button_clicked)
button.grid(column=1, row=1)
button.config(padx=3, pady=3)
input= Entry(width=25)
my_label.grid(column=0, row=0)
input.grid(column=3, row=3)

# text=Text(width=30, height=5)
# text.grid(column=3,row=3)
# text.focus()
# text.insert(END, 'this our text area')


buttonw= Button(text="clicked me ", command=button_clicked)
buttonw.grid(column=2, row=0)


window.mainloop()