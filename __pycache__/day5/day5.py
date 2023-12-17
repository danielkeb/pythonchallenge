# fruits=["apple", "banana", "ananas"]
# inp=input("enter separe")
# n=inp.split(",")
# print(n)
# for i in fruits:
#     print(i)

maxs=input("enter the number of students score").split()
for i in range(0,len(maxs)):
    maxs[i] = int(maxs[i])
high=0
for i in maxs:
    if i > high:
        high = i
print(f"maximum number of students scores: {high}")