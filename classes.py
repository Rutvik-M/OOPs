class Student:
    

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender =gender
    
    def display(self):
        print(f"My name is {self.name} , Age is {self.age} , and Gender is {self.gender}")


s1=Student()
s1.display()
