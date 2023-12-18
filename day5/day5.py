# fruits=["apple", "banana", "ananas"]
# inp=input("ennter separe")
# n=inp.split(",")
# print(n)
# for i in fruits:
#     print(i)
# th=0
# student_heights=input("enter studentS height").split()
# for n in range(0,len(student_heights),1):
#     student_heights[n]=int(student_heights[n])
   
#     th+=student_heights[n]
# nstd=0
# for std in range(0,len(student_heights)):
#     nstd+=1
# avg=th / nstd
# print(f"average of student heights: {avg}")

maxs=input("enter the number of students score").split()
for i in range(0,len(maxs)):
    maxs[i] = int(maxs[i])
high=0
for i in maxs:
    if i > high:
        high = i
print(f"maximum number of students scores: {high}")
