from tkinter import *
window=Tk()
window.title("Mile to Km Converter")
window.minsize(width=600, height=400)
window.config(padx=100,pady=50)

miles=Entry()
miles.grid(column=1, row=0)


def converter():
    kil=float(miles.get())

    result= round(kil * 1.609)
    kilometers.config(text=result)



label=Label(text="is equal to")
label.grid(column=0, row=1)
label.config(padx=5,pady=5)

klmtr=0
#klmtr=int(miles)
#miles.config(padx=5,pady=5)


kilometers=Label(text=0)
kilometers.grid(column=1, row=1)
kilometers.config(padx=5, pady=5)
                
mile=Label(text="Miles")
mile.grid(column=2, row=0)
mile.config(padx=5, pady=5)


kilometer=Label(text="Km")
kilometer.grid(column=2, row=1)
kilometer.config(padx=5,pady=5)



button= Button(text="Calculate",command=converter)
button.grid(column=1, row=2)
button.config(padx=5, pady=5)










window.mainloop()