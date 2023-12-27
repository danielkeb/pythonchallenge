student_score={
    "john":97,
    "jambo":86,
    "lema":76,
    "hailu":63,
}
empty_score={}
for thing in student_score:
    if student_score[thing]> 90 and student_score[thing]<=100:
        empty_score[thing] = "outstanding"
    elif student_score[thing] < 90 and student_score[thing]>80:
       empty_score[thing] = "exceeds expectations"
    elif student_score[thing]<80 and student_score[thing]>70:
        empty_score[thing] = "Acceptable"
    elif student_score[thing] < 70:
        empty_score[thing] = "failed"

print(empty_score)


