th=0
student_heights=input("enter studentS height").split()
for n in range(0,len(student_heights),1):
    student_heights[n]=int(student_heights[n])
   
    th+=student_heights[n]
nstd=0
for std in range(0,len(student_heights)):
    nstd+=1
avg=round(th / nstd)
print(f"average of student heights: {avg}")
