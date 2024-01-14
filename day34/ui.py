from tkinter import *
from quiz_brain import QuizBrain
from data import question_data
from question_model import Question
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain, ):
        self.quiz=quiz_brain

        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20,bg=THEME_COLOR)

        self.score_label=Label(text="Score:0",fg='white',bg=THEME_COLOR)
        self.score_label.grid(column=1,row=0)

        self.canvas=Canvas(width=300, height=250,bg='white')
        self.question_text=self.canvas.create_text(150,125, text='some question text',width=280,fill=THEME_COLOR)
        # self.canvas.config(padx=5,pady=5)
        self.canvas.grid(row=1,column=0, columnspan=2, padx=50, pady=50)

        
        false=PhotoImage(file='./images/false.png')
        self.button_false=Button(image=false, highlightthickness=0, command=self.false_answer)
        self.button_false.grid(column=0,row=2)

        true_image=PhotoImage(file='./images/true.png')
        self.true_button=Button(image=true_image, highlightthickness=0, command=self.true_answer)
        self.true_button.grid(column=1,row=2)

        self.get_next_question()


        self.window.mainloop()
    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.canvas.config(bg='white')
            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the question")
            self.true_button.config(state="disabled")
            self.button_false.config(state="disabled")


    def true_answer(self):
        is_right=self.quiz.check_answer("True")
        return self.givefeedback(is_right)
        
    
    def false_answer(self):
       is_right=self.quiz.check_answer("False")
       return self.givefeedback(is_right)
        
    
    def givefeedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)