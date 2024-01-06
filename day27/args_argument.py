def add(*args):
    print(args)
add(1,2,3,4,5,6,7,8)


def mult(n, **kwargs):


    n+=kwargs["add"]
    n*=kwargs["ad"]
        
    print(n)
mult(0, add=4,ad=2)



class Car:
    
    def __init__(self,**kw):
        self.make=kw["make"]
        self.model=kw["model"]

my_car=Car(make="haiundai",model="GT-R")
print(my_car.make)

