def add(n1,n2):
    return n1 + n2

def substract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2
def divide(n1,n2):
    return n1 / n2


calculator={
    "+":add,
    "-":substract,
    "*":multiply,
    "/":divide,
}
def calculator1():
    n1=int(input("enter first number: "))
    for thing in calculator:
        print(thing)

    cont=True
    while cont:
        oper=input("enter operator")
        n2=float(input("enter second number: "))
        calculator_fun=calculator[oper]
        aswer=calculator_fun(n1,n2)

        print(f"{n1} {oper} {n2} = {aswer}")
        ans= input(f"'y' to continue with {aswer} or start new type 'n' or you want exit program enter without n ,y")
        if ans=="y":
            n1=aswer

        elif ans=="n":
            cont=False
            calculator1()
        else:
            return 
            
calculator1()


       
    

