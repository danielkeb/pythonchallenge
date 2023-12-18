import math
def areaCalculator(height, width,coverage):
    
    needtobuy=math.ceil((height * width) / coverage)
    print(f"you will need to buy {needtobuy} cans")
height=int(input("enter the height"))
width=int(input("enter the width"))
coverage=5
areaCalculator(height,width,coverage)
