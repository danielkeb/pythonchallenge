def prime_checker(number,count):
    for i in range(1,number):
        if number%(i) == 0:
            count+=1
        else:
            count+=0
    if count>1:
        print("it's not a prime") 
    else:
        print("it's a prime")
number=int(input("check this number: "))
count=0
prime_checker(number,count)