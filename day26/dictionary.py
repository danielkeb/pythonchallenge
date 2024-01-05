name_list=['kidist','daniel','alemayehu','alem']
import random
student_score= {student: random.randint(1,100) for student in name_list}

print(student_score)


passed={student:score for (student,score) in student_score.items() if score >= 60}
print(f"passed student : {passed}") 