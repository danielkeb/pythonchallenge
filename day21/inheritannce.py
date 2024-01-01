class Animal:
    def __init__(self):
        self.anim_num=2

    def breathe(self):
        print("all animal breathing") 
class Fish(Animal):
    def __init__(self):
        super().__init__()
    def breathe(self):
        super().breathe()
        print("this is child class")
    
anim=Fish()

anim.breathe()