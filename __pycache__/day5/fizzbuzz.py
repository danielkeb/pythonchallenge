count=0
for i in range(1,101):
    if i%3==0 and i%5==0:
        count += 1
       
        print("fizzbuzz")
    elif i%3==0:
        count += 1
       
        print("fizz")
    elif i%5==0:
        count += 1
        
        print("buzz")
    else:
        print(i)
