class Student:
    name=""
    age=0
    gender=""

    def get_info(self,name ,age,gender):
        self.name=name
        self.age=age
        self.gender =gender
    
    def display(self):
        print(f"My name is {self.name} , Age is {self.age} , and Gender is {self.gender}")


s1=Student()
s1.get_info()
s1.display()

s2=Student()
s2.get_info()
s2.display()