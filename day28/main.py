import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
# import time

# count= 5

# while True:
#     time.sleep(1)
#     count-=1
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("promodoro")
#window.minsize(width=800, height=600)
window.config(padx=100, pady=50, bg=YELLOW)

reps=0
timer_btn =None
def start_timer():
   global reps
   reps += 1
   work_sec=WORK_MIN * 60
   short_break_sec = SHORT_BREAK_MIN * 60
   long_break_sec= LONG_BREAK_MIN * 60


   if reps%8 == 0:
        count_down(long_break_sec)
        timer.config(text="Break",fg=RED)

   if reps%2 == 0:
        count_down(short_break_sec)
        timer.config(text="Break",fg=PINK)
   else:
       count_down(work_sec)
       timer.config(text="Work",fg=GREEN)


def reset_timer():
    window.after_cancel(timer_btn)
    canvas.itemconfig(timer_text, text="00:00")
    timer.config(text="Timer")
    icon.config(text="")
    global reps
    reps =0


def count_down(count):
    count_min=math.floor(count / 60)
    count_sec= count % 60
   
    if count_sec < 10 :  # Convert count_sec to integer before comparison
       count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
     global timer_btn
     timer_btn = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks=""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
        icon.config(text=marks)


canvas=Canvas(width=200, height=224,bg=YELLOW, highlightthickness=0)
photo=PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=photo)


timer=Label(text="Timer",fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35,"bold"))
timer.grid(column=1, row=0)


timer_text=canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 35,"bold" ))
canvas.grid(column=1, row=1)
button=Button(text="Start",highlightthickness=0,command=start_timer)
button.grid(column=0, row=2)

reset=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset.grid(column=2, row=2, )

icon=Label(fg=GREEN, bg=YELLOW)
icon.grid(column=1,row=3)





window.mainloop()