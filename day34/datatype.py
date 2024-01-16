def police(age:int):
    if age > 18:
        return True
    else:
        return False
    
if police(2):
    print('yes you can drive car')
else:
    print("no you can't drive car")