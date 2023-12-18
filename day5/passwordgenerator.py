import random
alphabets=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K','L', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'b', 'd', 'e','f', 'g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','b','d','e','f']
numbers=['0','1','2','3','4','5','6','7','8','9']
especialsymbol=['~','%','&','*','!','(','-',')','+','$']
map=[alphabets,numbers,especialsymbol]
print("welcome to password generator")
passlength=int(input("Enter your password length: "))
symblo=int(input("how many input you want to use: "))
num=int(input("how many numbers you want to use: "))
password=""
for char in range(1,passlength + 1):
    letter=random.choice(alphabets)
    # for j in range(0,symblo):
    #         password += random.choice(symblo)
    # for k in range(0,num):
    #         password+= random.choice(numbers)
print(f"your generated password is: {letter}") 