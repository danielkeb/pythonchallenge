class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        
        if self.still_question():
            current_question = self.question_list[self.question_number]
            self.question_number += 1
            myans = input(f"Q. {self.question_number}: {current_question.text} (True/False): ")
            self.check_answer(myans, current_question.answer)
            is_on=True
        else:
            
            is_on=False

    def check_answer(self, myans, correct_answer):
        if myans.lower() == correct_answer.lower():
            self.score += 1
            print(f"You got it right!")
        else:
            print("You're wrong.")
        print(f"Correct answer was {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        final_score=self.score / self.question_number